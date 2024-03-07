from huggingface_hub import snapshot_download
import os


def handler(event, context):
    model = os.getenv("MODEL_ID")
    print("start download %s!"%model)
    snapshot_download(repo_id=model, revision="main")
    print("finish download %s!"%model)