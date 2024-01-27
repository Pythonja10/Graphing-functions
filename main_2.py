from tkinter import *
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import warnings
import matplotlib.pyplot as plt
import decimal

def asymptote_checker(a, f):
    try:
        f(a)
        return True
    except:
        return False
      
def evaluate(event):
      try:
            mystr = entry.get()
            exec('f = lambda x:' + mystr, globals())
            a = float(strA.get())
            b = float(strB.get())
            c = strC.get()
            if c=='auto':
                  if b-a <=1000:
                        c=0.01
                  elif b-a <=100000:
                        c=1
                  elif b-a <=10000000:
                        c=100
                  else:
                        c=10000
            else:
                  c=float(c)
                  if c*10000000<abs(a)+abs(b):
                        showerror('Ошибка', "Слишком маленький шаг")
                        return
            X = [round(x, 4) for x in arange(a, b, c)]
            Y = [f(x) if asymptote_checker(x, f) else float('nan') for x in X]
            ax.plot(X,Y)
            ax.grid(color='red', alpha=0.5, linestyle='dashed', linewidth=0.5)
            canvasAgg.draw()  # перерисовать "составной" холст
            return
      except:
            showerror('Ошибка', "Неверное выражение или интервал [a,b].")
            
#except:  # реакция на любую ошибку
     #showerror('Ошибка', "Неверное выражение или интервал [a,b].")


def evaluate2(event):  # чтобы кнопка отжималась при ошибке
    root.after(100, evaluate, event)

root = Tk()
root.title("График функции")
root.geometry('520x473+300+100')
warnings.filterwarnings("error")
#frameUp = Frame(root, relief=SUNKEN, height=64)
#frameUp.grid(side=TOP, fill=X)
Label(root, text="Выражение: ").grid(row=1,column=0,stick='wens')
Label(root, text="Начало интервала x:").grid(row=1,column=1,stick='wens')
Label(root, text="Конец интервала x:").grid(row=1,column=2,stick='wens')
Label(root, text="Шаг:").grid(row=1,column=3,stick='wens')
entry = Entry(root, relief=RIDGE, borderwidth=4)
#entry.bind("<Return>", evaluate)
entry.grid(row=2,column=0,stick='wens')
strA = StringVar()
strA.set(0)
entryA = Entry(root, relief=RIDGE, borderwidth=4, textvariable=strA)
entryA.grid(row=2,column=1,stick='wens')
#entryA.bind("<Return>", evaluate)
strB = StringVar()
strB.set(1)
entryB = Entry(root, relief=RIDGE, borderwidth=4, textvariable=strB)
entryB.grid(row=2,column=2,stick='wens')
strC = StringVar()
strC.set('auto')
entryC = Entry(root, relief=RIDGE, borderwidth=4, textvariable=strC)
entryC.grid(row=2,column=3,stick='wens')
#entryB.bind("<Return>", evaluate)
btn = Button(root, text='Создать')
btn.bind("<Button-1>", evaluate2)
btn.grid(row=3,column=0,stick='wens')
#root.bind('<Esc>', lambda event: root.destroy())
fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(111)
canvasAgg = FigureCanvasTkAgg(fig, master=root)
canvasAgg.draw()
canvas = canvasAgg.get_tk_widget()
canvas.grid(row=0,column=0,columnspan=4,stick='wens')

btn_1=Button(root,text='Очистить',command=lambda: ax.clear())
btn_1.grid(row=3,column=1,stick='wens')

root.mainloop()
