# coding:utf-8
#欢迎使用！[by link]
import random
import time
from tkinter import *
from tkinter.ttk import *

def clicked():
    global A
    global A1
    global B
    global B1
    global l1
    global out1
    global start
    global dur
    global dur1
    l1=[]
    out=''
    out1=''
    A = 0
    B = 0
    A1 = 'A'
    B1 = 'B'
    in1=int(combo.get())
    in2=int(combo1.get())
    result_data_Text.delete(1.0,END)
    result_data_Text1.delete(1.0,END)
    start=time.perf_counter()
    for i in range(in2):
        out=out+'\n----------第{}次重复试验----------\n'.format(i+1)
        for i in range(in1):
            rand_int = random.randint(1,10000)
            if rand_int <= 5000:
                A = A+1
                out=out+'<{}>'.format(A1)
            elif rand_int > 5000:
                B = B+1
                out=out+'<{}>'.format(B1)
        out=out+'\n----------结束----------\n'
        out=out+'结果:A{}次,B{}次'.format(A, B)
        l1.append([A,B])
        A=0
        B=0
    result_data_Text.insert(1.0,out)
    dur=time.perf_counter()-start
    start=time.perf_counter()
    for i in range(len(l1)):
        A=A+l1[i][0]
        B=B+l1[i][1]
    dur1=time.perf_counter()-start
    result_data_Text1.insert(1.0,'\n计算完毕，循环耗时{:.2f}s,计算耗时{:.5f}s'.format(dur,dur1))
    result_data_Text1.insert(1.0,'最终结果：\nA共{}次，B共{}次\n由数据可知，A:B基本为1:1，故生男生女概率相同。\n'.format(A,B))
window = Tk()
window.title("模拟试验")
window.geometry("700x800+300+3")
lbl = Label(window, text="         抓取次数:")
lbl.grid(column=0, row=0)
lbl1 = Label(window, text="         重复次数:")
lbl1.grid(column=0, row=8)
combo = Combobox(window)
combo1 = Combobox(window)
combo['values'] = (1,3,5,10,20,40,50,100,500,1000,1500)
combo1['values'] = (1,10,20,100,300,1000)
combo.current(2)
combo1.current(2)
combo.grid(column=8, row=0)
combo1.grid(column=8, row=8)
btn = Button(window, text="开始", command=clicked)
btn.grid(column=8, row=16)
result_data_Text = Text(window, width=70, height=13)
result_data_Text.grid(row=888, column=8)
result_data_Text1 = Text(window, width=70, height=29)
result_data_Text1.grid(row=100, column=8)
window.mainloop()
