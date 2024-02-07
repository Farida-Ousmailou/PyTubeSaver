# Projet "pytubesaver"

#module pytube
from pytube import YouTube

"""Ce programme utilise le module pytube afin de créer deux fonctions permettant succèssivement de télécharger et
 l'extractions des métadpnnées sur n'importe quelle vidéo youtube"""

def Download_video(url, emplacement):
    try:
        #Création d'objet YouTube avec l'URL de la vidéo
        #youtube_video = YouTube(url)

        # Afficher la liste des streams
        print("STREAMS")
        for stream in youtube_video.streams.fmt_streams:
            print(" ", stream)
        #Choix de la plus haute résolution
        stream = youtube_video.streams.get_highest_resolution()
        print("Stream vidéo: ", stream)

        #Information sur le niveau de progression du téléchargement
        def Download_progress(stream, chunk, bytes_remaining):
            bytes_downloaded = stream.filesize - bytes_remaining
            pourcentage = bytes_downloaded * 100 / stream.filesize
            print(f"Progression du téléchargement: {int(pourcentage)}%")

        #Téléchargement de la vidéo avec l'avénénement de la progression
        print("Téléchragement en cours")
        youtube_video.register_on_progress_callback(Download_progress)
        stream.download()
        print("Fin de téléchargement")

    except:
        print(f"Une erreur s'est produites")

#Extractions des métadpnnées

"""print("Titre: " + youtube_video.title)
    print("NB VUES: ", youtube_video.views)"""


#Demande à l'utilisateur l'url et l'emplacement de la vidéo sur son repertoire
url_vidéo = input("Entrez l'URL de la vidéo YouTube : ")
Emplacement_vidéo = input ("Entrez le chemin du repertoire de destination : ")

#Création d'objet YouTube avec l'URL de la vidéo
youtube_video = YouTube(url_vidéo)

#Appel de la fonction Download vidéo
Download_video(url_vidéo, Emplacement_vidéo)
