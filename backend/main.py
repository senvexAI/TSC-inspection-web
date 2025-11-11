# app/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json, os
from ocr import extract_text_from_image

app = FastAPI()

# --- CORS 허용 (Vercel frontend 접근 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 매핑 데이터 로드
with open("backend/data/mapping.json", "r", encoding="utf-8") as f:
    FILE_MAP = json.load(f)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """
    카메라 촬영 이미지 → OCR → 대응 PDF 반환
    """
    image_bytes = await file.read()
    text = extract_text_from_image(image_bytes)

    if text and text in FILE_MAP:
        pdf_path = FILE_MAP[text]
        return JSONResponse({"status": "ok", "member": text, "pdf_url": f"/{pdf_path}"})
    else:
        return JSONResponse({"status": "not_found", "recognized": text})

@app.get("/static/pdf/{filename}")
async def get_pdf(filename: str):
    """PDF 파일을 직접 반환"""
    filepath = f"backend/static/pdf/{filename}"
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/pdf")
    else:
        return JSONResponse({"error": "file not found"})
