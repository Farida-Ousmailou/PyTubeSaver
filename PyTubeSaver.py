# Projet "pytubesaver"
# module pytube

from pytube import YouTube

url = "https://www.youtube.com/watch?v=XSy6ADgadoU"
def Download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    pourcentage = bytes_downloaded * 100 / stream.filesize
    print(f"Progression du téléchargement: {int(pourcentage)}%")

# Création de l'objet Youtube
youtube_video = YouTube(url)

print("Titre: " + youtube_video.title)
print("NB VUES: ", youtube_video.views)

# Listes des streams
print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(" ", stream)

stream = youtube_video.streams.get_highest_resolution()
print("Stream vidéo: " , stream)

youtube_video.register_on_progress_callback(Download_progress)

print("Téléchragement en cours")
stream.download()
print("Fin de téléchargement")