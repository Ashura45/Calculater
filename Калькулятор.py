import tkinter as tk
import math


# Функции для выполнения операций
def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)
    clear_error()  # Очищаем ошибку при вводе новых данных


def clear():
    entry.delete(0, tk.END)
    clear_error()  # Очищаем ошибку при очистке


def calculate():
    expression = entry.get()  # Сохраняем вводимое выражение
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        # Добавляем вычисление в историю как исходное выражение
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, expression + " = " + str(result) + "\n")
        history_text.config(state=tk.DISABLED)
        history_text.yview(tk.END)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")
        # Ожидаем 0.5 секунды и очищаем сообщение об ошибке
        window.after(500, clear_error)


def clear_error():
    """Очищаем сообщение об ошибке, если оно есть."""
    if entry.get() == "Ошибка":
        entry.delete(0, tk.END)


def square():
    """Возведение в степень 2."""
    current_text = entry.get()
    try:
        result = float(current_text) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def power():
    current_text = entry.get()
    try:
        base, exp = current_text.split('^')  # Ожидаем формат "число^степень"
        base = float(base)
        exp = float(exp)
        result = base ** exp
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


def square_root():
    """Извлечение квадратного корня."""
    current_text = entry.get()
    try:
        result = math.sqrt(float(current_text))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор с Историей")

# Создаем поле ввода
entry = tk.Entry(window, width=25, font=("Arial", 14), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Создаем окно для истории
history_label = tk.Label(window, text="История вычислений", font=("Arial", 12))
history_label.grid(row=0, column=4, padx=10)

history_text = tk.Text(window, width=30, height=10, font=("Arial", 12), wrap=tk.WORD, state=tk.DISABLED)
history_text.grid(row=1, column=4, rowspan=5, padx=10, pady=10)


# Функция для включения/выключения истории
def toggle_history():
    if history_text.cget("state") == tk.DISABLED:
        history_text.config(state=tk.NORMAL)
        history_text.delete(1.0, tk.END)
    else:
        history_text.config(state=tk.DISABLED)


# Кнопка для очистки истории
clear_history_button = tk.Button(window, text="Очистить Историю", width=15, height=2, font=("Arial", 12),
                                 command=toggle_history)
clear_history_button.grid(row=6, column=4)

# Создаем кнопки калькулятора
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), #('²', 5, 3)
]

# Добавляем кнопки на экран
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == "C":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    elif text == "²":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=square)
    #elif text == "^":
        #button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=power)
    elif text == "√":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=square_root)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda value=text: click_button(value))

    button.grid(row=row, column=col)

# Запускаем главный цикл
window.mainloop()