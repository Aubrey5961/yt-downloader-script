import yt_dlp
from pathlib import Path
from yt_dlp import YoutubeDL

success_count = 0
fail_count = 0

def status(d):
    global success_count, fail_count

    if d['status'] == 'finished':
        print(f"✅ Finished downloading: {d['info_dict'].get('title', 'Unknown title')}")
        success_count += 1

    elif d['status'] == 'error':
        print(f"❌ Failed: {d.get('filename', 'Unknown file')}")
        fail_count += 1


download_folder = Path("<destination path>")
download_folder.mkdir(parents=True, exist_ok=True)

video_url = {
    "<youtube link>",   
}

video_options = {
    'outtmpl' : str(download_folder / '%(title)s.%(ext)s'),
    'format' : 'bestvideo+bestaudio/best',
    'merge_output_format' : 'mkv', # file type of .mkv
    'progress_hooks' : [status], # status updates
}

with yt_dlp.YoutubeDL(video_options) as ydl:
    try:
        ydl.download(video_url)
    
    finally:
        print("\n=== Download Summary ===")
        print(f"Successful downloads: {success_count}")
        print(f"Failed downloads: {fail_count}")
        print("All downloads completed.")

