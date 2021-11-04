""""
@author ROMAIN LE TALOUR
THIS PROGRAMME IS MEANT TO DOWNLOAD VIDEOS FROM YOUTUBE
ENJOY
"""

from pytube import YouTube;

import os

print("==== YouTube Downloader ==== \n")

"""
    Function to download a Youtube video selecting the quality
"""
def video_download():
    link = input("Coller le lien de la vidéo ci-dessous \n")
    yt = YouTube(link)

    print(yt.title, '\n')

    # List of available streams to download
    mp4_streams = yt.streams.filter(file_extension='mp4')
    for i in mp4_streams:
        print(i)

    # Downloading
    print('\n \n')
    itag = input("Entrer le flux vidéo voulu (copier le numéro de itag):")
    stream = yt.streams.get_by_itag(itag)

    username = os.getenv("USERNAME")
    username = str(username)

    output_path = 'C:\\Users\\' + username + '\\Video'

    print('\n \n')
    print("Téléchargement dans " + output_path)

    stream.download(output_path)

    print('Terminé !')

if __name__ == '__main__':
    video_download()
