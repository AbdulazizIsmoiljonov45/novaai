from google import genai

# API kalitingiz
client = genai.Client(api_key="AIzaSyAw248s0YapTyYh6yX5u3OilCa87xNR6Ow")

# Model nomini "models/gemini-1.5-flash" ko'rinishida yozib ko'ramiz
MODEL_ID = "models/gemini-1.5-flash"

def nova_ai():
    print("--- Nova AI tizimi ishga tushdi ---")
    
    while True:
        try:
            user_input = input("\nSiz: ")
            
            if user_input.lower() in ['chiqish', 'stop', 'exit']:
                break

            # So'rov yuborish
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=f"Isming Nova. Savolga javob ber: {user_input}"
            )
            
            print(f"\nNova: {response.text}")
            
        except Exception as e:
            # Agar models/ bilan ham ishlamasa, shunchaki "gemini-1.5-flash" ni qayta urinib ko'radi
            print(f"\nXatolik yuz berdi: {e}")
            print("Modelni qayta tekshirib ko'ring yoki API kalit ruxsatlarini ko'ring.")
            break

if __name__ == "__main__":
    nova_ai()
