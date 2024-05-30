import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('library_catalog.db')

# Создаем курсор для работы с базой данных
cursor = conn.cursor()

# Создаем таблицу для книг
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Вставляем пример данных в таблицу
cursor.execute('''
    INSERT INTO books (title, author, year) VALUES
    ('Преступление и наказание', 'Федор Достоевский', 1866),
    ('Война и мир', 'Лев Толстой', 1869),
    ('1984', 'Джордж Оруэлл', 1949)
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
