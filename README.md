# 🧠 Automating Image Captioning using BLIP and n8n

This project automates the process of image captioning using [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-large), a low-code automation platform **n8n**, and Google Sheets.

Whenever a new image is saved to the `to_process/` folder:
- The image is automatically captioned using a **BLIP model** hosted via Colab/ngrok.
- The image path and caption are stored in **Google Sheets**.
- The image is **renamed to its caption** and moved to a `processed/` folder.

<br/>

## 📦 Features

- 📸 Watch a folder for new images
- 🤖 Auto-generate captions using `Salesforce/blip-image-captioning-large`
- 📄 Log captions to Google Sheets
- 🔁 Rename images based on captions
- 🚚 Move processed images to a new folder
- ⚙️ Fully automated with `n8n`

<br/>

## 🚀 How It Works

1. **Place image** in the `to_process/` folder.
2. `watcher.py` detects new files and sends the image to an **n8n webhook**.
3. n8n sends the image to a BLIP model hosted via **Colab + ngrok**.
4. Caption is returned and:
   - Stored to **Google Sheets**
   - Sent to `mover.py` along with original image path
5. `mover.py` renames the file to the caption and moves it to the `processed/` folder.

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anuragpathak27/Automating-Image-Captioning-using-BLIP-and-n8n.git
cd Automating-Image-Captioning-using-BLIP-and-n8n
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run mover.py API
```bash
python mover.py
```

- This listens on http://localhost:5050/move
- Accepts POST requests with:
```bash
{
  "image_path": "...",
  "caption": "..."
}
```

### 4. Run watcher.py to Monitor Folder
```bash
python watcher.py
```

- Watches the to_process/ folder
- Sends any new image to your n8n Webhook

### 5. Set Up and Run n8n (Free Version)
- Option A: Run via Docker
```bash
docker-compose up -d
```

Then open http://localhost:5678 in your browser.

- Option B: Use n8n Cloud (Optional, Paid)

### 6. Import the Workflow

1. Open n8n
2. Click "Import" in the top menu
3. Select n8n-workflow.json from this repo
4. Update:
   - Webhook URL
   - ngrok BLIP API endpoint
   - Google Sheet ID and column mappings

### 📜 License
This project is open source and available under the MIT License.

### Author 
Anurag Pathak
