markdown
# Habr Top Daily Parser

Парсер, который получает список самых популярных статей за день с сайта Habr и выводит в консоль заголовки и количество просмотров.

## Ссылка на проект
[Проект на solvit.space](https://solvit.space/projects/habr_parser)

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Sunknn/habr-parser.git
   cd habr-parser
Создайте виртуальное окружение и активируйте его:

bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate     # для Windows
Установите зависимости:

bash
pip install -r requirements.txt
Запустите парсер:

bash
python parser.py
Пример вывода
text
1. Родина-мама, не бряцай оружьем | Просмотры: 30K
2. Топ известных и мемных роботов... | Просмотры: 12K
...
Используемые технологии
Python 3

requests

BeautifulSoup4

text

---

## 🚀 После создания – залей на GitHub

В терминале (всё ещё с `(venv)`) выполни:

```bash
git add README.md
git commit -m "Добавлен README с ссылкой на проект"
git push
