def hello_world():
    """Базовая функция приветствия"""
    return "Hello, World!"

def hello_name(name):
    """Функция приветствия с именем"""
    if not name or name.strip() == "":
        return "Hello, Anonymous!"
    return f"Hello, {name}!"

class Greeter:
    """Класс для управления приветствиями"""
    
    def __init__(self, language="en"):
        self.language = language
        self.greetings = {
            "en": "Hello",
            "es": "Hola",
            "fr": "Bonjour"
        }
    
    def greet(self, name=None):
        greeting = self.greetings.get(self.language, self.greetings["en"])
        if not name or name.strip() == "":
            return f"{greeting}, Anonymous!"
        return f"{greeting}, {name}!"

def main():
    # Старые функции для обратной совместимости
    print(hello_world())
    print(hello_name("User"))
    
    # Новая функциональность
    greeter = Greeter("en")
    print(greeter.greet("Alice"))
    
    greeter_es = Greeter("es")
    print(greeter_es.greet("Carlos"))

if __name__ == "__main__":
    main()
