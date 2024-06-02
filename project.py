import sqlite3
from tkinter import Tk, Label, Entry, Button

# Функция для добавления книги в базу данных
def add_book(title, author, year):
    conn = sqlite3.connect('library_catalog.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    conn.commit()
    conn.close()

# Функция, вызываемая при нажатии кнопки
def on_submit():
    add_book(title_entry.get(), author_entry.get(), year_entry.get())

# Создаем главное окно
root = Tk()
root.title('Библиотечный каталог')

# Создаем виджеты
title_label = Label(root, text='Название:')
title_entry = Entry(root)
author_label = Label(root, text='Автор:')
author_entry = Entry(root)
year_label = Label(root, text='Год издания:')
year_entry = Entry(root)
submit_button = Button(root, text='Добавить', command=on_submit)

# Располагаем виджеты
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)
author_label.grid(row=1, column=0)
author_entry.grid(row=1, column=1)
year_label.grid(row=2, column=0)
year_entry.grid(row=2, column=1)
submit_button.grid(row=3, column=1)

# Запускаем главный цикл
root.mainloop()

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
