def hello_world():
    """Базовая функция приветствия"""
    return "Hello, World!"

def hello_name(name):
    """Новая функция приветствия с именем"""
    return f"Hello, {name}!"

def main():
    print(hello_world())
    # Демонстрация новой функциональности
    print(hello_name("User"))

if __name__ == "__main__":
    main()
