import tkinter

win = tkinter.Tk()
win.title("Grid Example")
win.geometry("300x300")

b1=tkinter.Button(win, text="(0,0)")
b2=tkinter.Button(win, text="(0,1)", width=20)
b3=tkinter.Button(win, text="(0,2)")

b4=tkinter.Button(win, text="(1,0)")
b5=tkinter.Button(win, text="(1,1)")
b6=tkinter.Button(win, text="(1,3)")

b7=tkinter.Button(win, text="(2,1)")
b8=tkinter.Button(win, text="(2,2)")
b9=tkinter.Button(win, text="(2,4)")

#grid: 셀단위 배치, pack은 같이 사용 안됨 place는 ㄱㅏ능
#가장 처음 작성한 grid부터 우선 배치

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0, rowspan=2)
b5.grid(row=1, column=1, columnspan=3)
b6.grid(row=1, column=3)

b7.grid(row=2, column=1, sticky="w")
b8.grid(row=2, column=2)
#column이 99여도 이전에 column 최대값이 3이라서 자동으로 4 할당
b9.grid(row=2, column=99)



win.mainloop()