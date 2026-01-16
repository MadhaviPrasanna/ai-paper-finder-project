import os
import sys
import datetime
from huggingface_hub import snapshot_download
import uvicorn
import runpy

print(f"===== Application Startup at {datetime.datetime.now():%Y-%m-%d %H:%M:%S} =====")

# ---------------- CONFIG ----------------
REPO_ID = "wenhanacademia/ai_paper_finder"   # private repo with full app + DB
HF_TOKEN = os.getenv("HF_TOKEN", "").strip()  # stored as secret
# -----------------------------------------

print(f"Downloading repo {REPO_ID} ...")
repo_dir = snapshot_download(repo_id=REPO_ID, token=HF_TOKEN)
print(f"Repo downloaded to: {repo_dir}")
os.environ["APP_ROOT"] = repo_dir # For database

uvicorn.run(
    "backend.main:app",
    host="0.0.0.0",
    port=7860,
)
