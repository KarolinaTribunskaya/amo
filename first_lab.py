from tkinter import *
from tkinter import messagebox
import random
import math
import subprocess
import file1_lab1 as f1
import file2_lab1 as f2
# from Pillow import Image

# img = Image.open('logo.png')
# img.show()

# import os
# os.system("logo.png")

#from matplotlib import pyplot as plt


#img = plt.imread('x.jpg')
#plt.imshow(img)
#plt.show()

root = Tk()
root.geometry("600x600")
root.title("Алгоритми та методи обчислень")


def linear_algorithm():
    global task1_image_link
    win1 = Toplevel(root)

    def result1():
        try:
            x = float(entry_x.get())
            y = float(entry_y.get())
            z = float(entry_z.get())
            g = float(entry_g.get())
            h = float(entry_h.get())
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")

        try:
            y1_answer = ((z + y) ** (g + h)) / ((z + x) ** ((g + h) / (g * h)))
            y1["text"] = "\n\nY1 = {}".format(y1_answer)
        except:
            messagebox.showinfo("Помилка", "Обрахунки неможливі!")


    def edit_data():
        subprocess.call(["notepad.exe", "file1_lab1.py"])


    def result1_2():
        try:
            x = f1.x
            y = f1.y
            z = f1.z
            g = f1.g
            h = f1.h
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")

        try:
            y1_answer = ((z + y) ** (g + h)) / ((z + x) ** ((g + h) / (g * h)))
            y1["text"] = "\n\nY1 = {}\n".format(y1_answer)
        except:
            messagebox.showinfo("Помилка", "Обрахунки неможливі!")

    # значки
    task1 = Label(win1, text="Завдання 1\nЛінійний алгоритм\n")

    entry_x = Entry(win1)
    entry_y = Entry(win1)
    entry_z = Entry(win1)
    entry_g = Entry(win1)
    entry_h = Entry(win1)

    label_x = Label(win1, text="Введіть значення х")
    label_y = Label(win1, text="Введіть значення y")
    label_z = Label(win1, text="Введіть значення z")
    label_g = Label(win1, text="Введіть значення g")
    label_h = Label(win1, text="Введіть значення h")

    label_task1 = Label(win1, text="\nФормула, за якою \nбудуть виконуватися обчислення:")

    task1_image = Label(win1, image=task1_image_link)

    result_button1 = Button(win1, text="Зчитати дані й \nобрахувати результат", command=result1,
                            activebackground="green")

    edit_button = Button(win1, text="Редагувати дані змінних у файлі", command=edit_data,
                            activebackground="green")

    result_button2 = Button(win1, text="Зчитати дані з файлу \nй обрахувати результат", command=result1_2,
                            activebackground="green")
    y1 = Label(win1, text="\n\nY1 = \n")

    # пакування
    task1.grid(column=1, row=1)

    entry_x.grid(column=1, row=3)
    entry_y.grid(column=1, row=5)
    entry_z.grid(column=1, row=7)
    entry_g.grid(column=1, row=9)
    entry_h.grid(column=1, row=11)

    label_x.grid(column=1, row=2)
    label_y.grid(column=1, row=4)
    label_z.grid(column=1, row=6)
    label_g.grid(column=1, row=8)
    label_h.grid(column=1, row=10)

    label_task1.grid(column=1, row=14)
    task1_image.grid(column=1, row=15)
    result_button1.grid(column=1, row=16)
    edit_button.grid(column=1, row=17)
    result_button2.grid(column=1, row=18)
    y1.grid(column=1, row=19)


def tree_algorithm():
    global task2_image_link
    win2 = Toplevel(root)

    def result2():
        try:
            v = float(entry_v.get())
            b = float(entry_b.get())
            g = float(entry_g_2.get())
            s = float(entry_s.get())
            t = float(entry_t.get())
            y = float(entry_y_2.get())
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")

        try:
            y2_answer = math.sqrt(24 * g - s * b - (y * t) / (v * b))
            y2["text"] = "\n\nY = {}".format(y2_answer)
        except:
            messagebox.showinfo("Помилка", "Обрахунки неможливі!")

    def edit_data():
        subprocess.call(["notepad.exe", "file2_lab1.py"])

    def result2_1():
        try:
            v = f2.v
            b = f2.b
            g = f2.g
            s = f2.s
            t = f2.t
            y = f2.y
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")

        try:
            y2_answer = math.sqrt(24 * g - s * b - (y * t) / (v * b))
            y2["text"] = "\n\nY = {}".format(y2_answer)
        except:
            messagebox.showinfo("Помилка", "Обрахунки неможливі!")


    task2 = Label(win2, text="Завдання 2\nАлгоритм, що розгалужується\n\n")
    entry_v = Entry(win2)
    entry_b = Entry(win2)
    entry_g_2 = Entry(win2)
    entry_s = Entry(win2)
    entry_t = Entry(win2)
    entry_y_2 = Entry(win2)

    label_v = Label(win2, text="Введіть значення v")
    label_b = Label(win2, text="Введіть значення b")
    label_g_2 = Label(win2, text="Введіть значення g")
    label_s = Label(win2, text="Введіть значення s")
    label_t = Label(win2, text="Введіть значення t")
    label_y_2 = Label(win2, text="Введіть значення y")

    label_task2 = Label(win2, text="\nФормула, за якою \nбудуть виконуватися обчислення:")

    task2_image = Label(win2, image=task2_image_link)

    result_button2 = Button(win2, text="Зчитати дані й \nобрахувати результат", command=result2,
                            activebackground="green")

    edit_button = Button(win2, text="Редагувати дані змінних у файлі", command=edit_data,
                         activebackground="green")

    result_button3 = Button(win2, text="Зчитати дані з файлу \nй обрахувати результат", command=result2_1,
                            activebackground="green")
    y2 = Label(win2, text="\n\nY = ")


    # task2 pack
    task2.grid(column=2, row=1)

    entry_v.grid(column=2, row=3)
    entry_b.grid(column=2, row=5)
    entry_g_2.grid(column=2, row=7)
    entry_s.grid(column=2, row=9)
    entry_t.grid(column=2, row=11)
    entry_y_2.grid(column=2, row=13)

    label_v.grid(column=2, row=2)
    label_b.grid(column=2, row=4)
    label_g_2.grid(column=2, row=6)
    label_s.grid(column=2, row=8)
    label_t.grid(column=2, row=10)
    label_y_2.grid(column=2, row=12)

    label_task2.grid(column=2, row=14)
    task2_image.grid(column=2, row=15)
    result_button2.grid(column=2, row=16)
    edit_button.grid(column=2, row=17)
    result_button3.grid(column=2, row=18)

    y2.grid(column=2, row=19)


def cycle_algorithm():
    global task3_image_link
    win3 = Toplevel(root)

    def result3():
        try:
            arr = (entry_arr.get()).split()
            print(arr)
            for i in range(len(arr)):
                arr[i] = float(arr[i])
            print(arr)
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")

        try:
            y3_answer = 1
            for i in arr:
                y3_answer *= 1/i
            y3["text"] = "\n\nY = {}".format(y3_answer)
        except:
            messagebox.showinfo("Помилка", "Обрахунки неможливі!")

    task3 = Label(win3, text="Завдання 3\nЦиклічний алгоритм\n")
    entry_arr = Entry(win3)

    label_arr = Label(win3, text="Через пробіл введіть значення n1 n2 n3 ... n15")

    label_task3 = Label(win3, text="\nФормула, за якою \nбудуть виконуватися обчислення:")

    task3_image = Label(win3, image=task3_image_link)

    result_button3 = Button(win3, text="Зчитати дані й \nобрахувати результат", command=result3,
                            activebackground="green")
    y3 = Label(win3, text="\n\nf = ")


    # task3 pack
    task3.grid(column=2, row=1)
    entry_arr.grid(column=2, row=3)
    label_arr.grid(column=2, row=2)

    label_task3.grid(column=2, row=5)
    task3_image.grid(column=2, row=6)
    result_button3.grid(column=2, row=7)
    y3.grid(column=2, row=8)


mainmenu = Menu(root)
root.config(menu=mainmenu)


lab1 = Menu(mainmenu, tearoff=0)

lab1.add_command(label="Лінійний алгоритм", command=linear_algorithm)
lab1.add_command(label="Розгалужений алгоритм", command=tree_algorithm)
lab1.add_command(label="Циклічний алгоритм", command=cycle_algorithm)

mainmenu.add_cascade(label="Лабораторна робота 1",
                     menu=lab1)

task1_image_link = PhotoImage(file="task1_image.png")
task2_image_link = PhotoImage(file="task2_image.png")
task3_image_link = PhotoImage(file="task3_image.png")

hello = Label(root, text="Лабораторні роботи з предмету алгоритми та методи обчислень.\n"
                         "Щоб передивитися виконані лабораторні роботи скористайтеся \n"
                         "відповідними розділами меню")

hello.pack()


#subprocess.call(["word", "logo.png"])


root.mainloop()
# subprocess.call(["notepad.exe", "file1_lab1.py"])

