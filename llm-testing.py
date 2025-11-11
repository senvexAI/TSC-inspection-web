from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(override=True)

image_path = 'test.jpg'

def main():
    print("Hello from tsc-inspection-web!")
    client = genai.Client()
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    
    input_text = """what is the image saying?"""

    response_handwritten = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            (input_text),
        ],
    )
    print(response_handwritten)
    # raw_handwritten = response_handwritten.text.strip()
    # # 코드블록 백틱이 있을 경우 제거
    # if raw_handwritten.startswith("```"):
    #     raw_handwritten = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_handwritten, flags=re.DOTALL).strip()
    # handwritten_info = json.loads(raw_handwritten) 


if __name__ == "__main__":
    
    main()
