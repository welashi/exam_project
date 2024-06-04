import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.ttk import Treeview

# Функция для добавления книги в базу данных
def add_book(title, author, year):
    try:
        with sqlite3.connect('library_catalog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO books (title, author, year) VALUES (?, ?, ?)
            ''', (title, author, year))
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка базы данных", e)

# Функция для получения данных из базы данных
def view_books():
    try:
        with sqlite3.connect('library_catalog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books')
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка базы данных", e)
        return []

# Функция для удаления книги по ID
def delete_book(book_id):
    try:
        with sqlite3.connect('library_catalog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка базы данных", e)

# Функция для обновления данных в Treeview
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for row in view_books():
        tree.insert('', 'end', values=row)

# Функция для удаления столбца
def remove_column(column_name):
    try:
        with sqlite3.connect('library_catalog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('PRAGMA table_info(books)')
            columns = [info[1] for info in cursor.fetchall() if info[1] != column_name]
            cursor.execute(f'CREATE TABLE books_new ({", ".join(columns)})')
            cursor.execute(f'INSERT INTO books_new SELECT {", ".join(columns)} FROM books')
            cursor.execute('DROP TABLE books')
            cursor.execute('ALTER TABLE books_new RENAME TO books')
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка базы данных", e)

# Функция, вызываемая при нажатии кнопки
def on_submit():
    add_book(title_entry.get(), author_entry.get(), year_entry.get())
    # Обновляем таблицу
    update_treeview()


# Создаем главное окно
root = Tk()
root.title('Библиотечный каталог')

# Создаем виджеты для ввода данных
title_label = Label(root, text='Название:')
title_entry = Entry(root)
author_label = Label(root, text='Автор:')
author_entry = Entry(root)
year_label = Label(root, text='Год издания:')
year_entry = Entry(root)
submit_button = Button(root, text='Добавить', command=on_submit)

# Создаем Treeview для отображения данных
tree = Treeview(root, columns=('ID', 'Title', 'Author', 'Year'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Title', text='Название')
tree.heading('Author', text='Автор')
tree.heading('Year', text='Год издания')

# Располагаем виджеты
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)
author_label.grid(row=1, column=0)
author_entry.grid(row=1, column=1)
year_label.grid(row=2, column=0)
year_entry.grid(row=2, column=1)
submit_button.grid(row=3, column=1)
tree.grid(row=4, column=0, columnspan=2)

# Запускаем главный цикл
root.mainloop()
