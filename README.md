SemVer Example Project

Простой проект для демонстрации семантического версионирования.

Система версионирования

Этот проект следует правилам Semantic Versioning 2.0.0:

- **MAJOR** версия (X.0.0) - при несовместимых изменениях API
- **MINOR** версия (0.X.0) - при добавлении новой функциональности
- **PATCH** версия (0.0.X) - при исправлении багов

Список релизов

v1.2.0 (Текущий)
- **Добавлено**: Мультиязычная поддержка через класс Greeter
- **Добавлено**: Английский, испанский, французский языки

#v1.1.1
- **Исправлено**: Обработка пустых имен в функции hello_name()

v1.1.0
- **Добавлено**: Функция персонализированного приветствия hello_name()

v1.0.0
- **Добавлено**: Базовая функция hello_world()

Использование

Базовое использование

from main import hello_world, hello_name

print(hello_world())      # "Hello, World!"
print(hello_name("Alice")) # "Hello, Alice!"
print(hello_name(""))      # "Hello, Anonymous!"
from main import Greeter

greeter_en = Greeter("en")
print(greeter_en.greet("Alice"))  # "Hello, Alice!"

greeter_es = Greeter("es")  
print(greeter_es.greet("Carlos")) # "Hola, Carlos!"

greeter_fr = Greeter("fr")
print(greeter_fr.greet("Marie"))  # "Bonjour, Marie!"

Процесс разработки
Новый функционал добавляется через feature-ветки

Каждое изменение проходит code review через Pull Requests

Версии назначаются согласно SemVer
