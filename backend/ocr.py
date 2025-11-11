from typing import Optional
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv(override=True)
# image_path = 'test.jpg'

def extract_text_from_image(image_bytes: bytes) -> Optional[str]:
    """
    이미지에서 부재명 추출 (임시 Mock 버전)
    """
    try:
        client = genai.Client()
        # with open(image_path, "rb") as f:
        #     image_bytes = f.read()
        
        input_text = """what is the image saying?"""

        response_handwritten = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                (input_text),
            ],
        )
        print(response_handwritten)

        recognized_text = "B1-01"  # Mock 예시
        
        return recognized_text
    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return None