def get_cats_info(path):
    cats_info = []
    
    try:
        cat = ["id", "name", "age"]
        with open (path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                
                cat_dict = {
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                }
                cats_info.append(cat_dict)
            
    except FileNotFoundError:
        print (f"Помилка: файл {path} не знайдено.")
    except IOError:
        print (f"Помилка: не вдалося прочитати файл {path}.")
    
        return cats_info
   
            














"""Вимоги до завдання:

Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


Рекомендації для виконання:

Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.


Критерії оцінювання:

Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим."""