import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

N8N_WEBHOOK_URL = "REPLACE_WITH_YOUR_N8N_WEBHOOK_URL"

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.lower().endswith((".png", ".jpg", ".jpeg")):
            time.sleep(1)  # wait for file write to finish
            full_path = os.path.abspath(event.src_path)
            print(f"[📸] New image: {full_path}")
            with open(full_path, 'rb') as f:
                files = {'image': (os.path.basename(full_path), f, 'image/jpeg')}
                response = requests.post(N8N_WEBHOOK_URL, files=files)
                print(f"[📤] Sent to n8n, Status: {response.status_code}")

if __name__ == "__main__":
    folder = "to_process"
    observer = Observer()
    observer.schedule(WatcherHandler(), path=folder, recursive=False)
    observer.start()
    print("👀 Watching folder...")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
