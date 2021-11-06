# 7. Напишите программу на python с графическим интерфейсом, которая запрашивает у
# пользователя 3 целых числа. Добавить кнопку “Посчитать”. После нажатия на кнопку
# “Посчитать” на экране в поле “Результат” выводятся только те числа, которые
# принадлежат интервалу (10, 20]. Использовать модуль TKinter.


from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Лабораторная работа 9")
root.geometry("800x500")

l_original_text = Label(text = "Введите 3 числа в диапазоне (10, 20]:", background = "#ccc", foreground =
"#444", font = "16")
l_original_text.pack()

t_original_text = Text(height = 5, background = "#fff", foreground = "#444", font =
"16")
t_original_text.pack()


l_result_text = Label(text = "числа, которые принадлежат интервалу (10, 20]:", background = "#ccc",foreground = "#444", font = "16")
l_result_text.pack()

t_result_text = Text(height = 5, background = "#fff", foreground = "#444", font =
"16")
t_result_text.pack()


def convert():
    text = t_original_text.get(1.0, END).replace("\n",'')
    numbers = text.split(' ')

    if len(numbers) != 3:
        messagebox.showinfo("!", "Введено невалидное количество значений")
        return

    result_string = ''

    i = 0
    while i < 3:
        if 10 < int(numbers[i]) < 21:
            result_string = result_string + numbers[i] + " "
        i += 1

    t_result_text.delete(1.0, END)
    t_result_text.insert(1.0, result_string)


btn_convert = Button(text = "Посчитать", command = convert)
btn_convert.pack()

root.mainloop()
