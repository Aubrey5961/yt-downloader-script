import yt_dlp
from pathlib import Path


download_folder = Path("<destination>")
download_folder.mkdir(parents=True, exist_ok=True)

vid_url = {
    "<url>",
}

vid_quality = {
    'outtmpl' : str(download_folder / '%(title)s.%(ext)s'),
    'format' : 'bestvideo+bestaudio/best',
    'merge_output_format' : 'mkv', # file type of .mkv
}

with yt_dlp.YoutubeDL(vid_quality) as ydl:
    ydl.download(vid_url)