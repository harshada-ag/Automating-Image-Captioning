from flask import Flask, request
import shutil, os, re

app = Flask(__name__)

def sanitize_filename(text):
    # Replace spaces with underscores, remove unsafe characters
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '_', text)

@app.route('/move', methods=['POST'])
def move_image():
    data = request.json
    print("[📥] Incoming JSON:", data)
    src = data.get("image_path")
    caption = data.get("caption")
    print(src)
    print(caption)

    if not os.path.exists(src):
        return {"error": "File not found"}, 404

    folder_dst = src.replace("to_process", "processed")
    folder_dst = os.path.dirname(folder_dst)

    ext = os.path.splitext(src)[1]
    safe_caption = sanitize_filename(caption)
    dst = os.path.join(folder_dst, f"{safe_caption}{ext}")

    os.makedirs(folder_dst, exist_ok=True)
    shutil.move(src, dst)
    return {"message": "Moved and Renamed", "new_path": dst}

if __name__ == "__main__":
    app.run(port=5050)
