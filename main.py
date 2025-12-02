from brain import TinyBrain

print("ChatAi Demo Lite — ИИ, который помнит навсегда")
brain = TinyBrain()
print("Привет! Я — Зёня. Я помню всё, что ты скажешь. Даже после перезагрузки.\n")

while True:
    user = input("Ты: ")
    if user.lower() in ["выход", "exit", "bye"]: 
        print("Зёня: Пока! Я всё запомнил ❤️")
        break
    reply = brain.think(user)
    print(f"Зёня: {reply}")
