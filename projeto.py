
import speech_recognition as sr

def reconhecer_fala():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("ajustando audio")
        recognizer.adjust_for_ambient_noise(source)
        print("Pronto para ouvir. Fale alguma coisa:")
        audio = recognizer.listen(source)
    
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print("você falou: " + texto)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError as e:
        print(f"não consegui entender, por favor repita")

reconhecer_fala()
