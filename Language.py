import tkinter as tk
from tkinter import ttk

# Словарь для хранения сообщений на разных языках
messages = {
    'english': {
        'hello': 'Hello, world!',
        'change_lang': 'Change Language'
    },
    'espanish': {
        'hello': 'Hola, mundo!',
        'change_lang': 'Cambiar idioma'
    }
}

def change_language(*args):
    # Получаем выбранный язык из выпадающего списка
    selected_lang = combo_var.get()
    
    # Обновляем текст на кнопке и метке согласно выбранному языку
    hello_label.config(text=messages[selected_lang]['hello'])
    change_lang_button.config(text=messages[selected_lang]['change_lang'])

root = tk.Tk()
root.title("Internationalization Example")

# Создаем объекты интерфейса
hello_label = tk.Label(root, text="Hello, world!", font=("Arial", 14))
hello_label.pack(pady=20)

# Создаем выпадающий список для выбора языка
combo_var = tk.StringVar()
language_combo = ttk.Combobox(root, textvariable=combo_var, values=['english', 'espanish'], state='readonly')
language_combo.pack()

change_lang_button = tk.Button(root, text="Change Language", command=change_language)
change_lang_button.pack(pady=10)

# Устанавливаем обработчик события при выборе языка из списка
combo_var.trace('w', change_language)

# Устанавливаем начальный язык (по умолчанию)
combo_var.set('english')
change_language()

root.mainloop()
