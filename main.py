import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import os
class hensuu:
    static_num = 1

path = os.getcwd()

#cppファイルを読み込み、その中身を返す
def read_cppfile(cppfile):
    print("cppファイルを読み込みます" + cppfile)
    with open(cppfile,"r") as rf:
        data = rf.read()
    return data

#exeファイルを引数ありで実行
def exe_with_arg(exefile,arg):
    print("exeファイルを実行します")
    arg_list = ""
    for a in arg:
        arg_list += a + " "
    a = os.system(f"echo {arg_list} | {exefile}")
    print(a)
    return str(a)
#課題のテキストファイルを出力(未)
def make_txtfile(problem_list):
    if problem_list[0][0].get() == "" or problem_list[0][1].get() == "" or problem_list[0][2].get() == "":
        return "入力されていません"
    elif not os.path.isfile(problem_list[0][0].get()):
        return "cppファイルが存在しません"
    elif not os.path.isfile(problem_list[0][2].get()):
        return "exeファイルが存在しません"

    i = 1
    pro = 0
    while(os.path.isfile(f"課題{i}.txt")):
        i += 1
    with open(f"課題{i}.txt","w") as wf:
        print(problem_list)
        for p in problem_list:
            jikkou = 1
            pro += 1
            wf.write(f"課題{pro}：" + "\n" + "「" + p[1].get() + "」\n")
            wf.write("作成したプログラム：\n" + read_cppfile(p[0].get()) + "\n")
            for j in p[3].get().split():
                wf.write(f"実行結果{jikkou}：　\n >./a.out \n" + exe_with_arg(p[2].get(),j) + "\n")
                jikkou += 1
    return "課題"+str(i)+".txtを作成しました"

#tkinterでのGUIの作成
def gui():
    root = tk.Tk()
    root.title("課題作成ヘルパー")
    root.geometry("500x300")
    entry_list = []

    def make_form():
        # Create new widgets
        label_problem = tk.Label(root,text=f"問題{hensuu.static_num//4+1}",bg="gray")
        entry_problem = tk.Entry(root,font=("Helvetica",10))
        label_cpp = tk.Label(root,text="cppの名前（pythonファイルと同じ場所に置くこと）",bg="white")
        entry_cpp = tk.Entry(root,font=("Helvetica",10),bg="white")
        label_exe = tk.Label(root,text="exeの名前（pythonファイルと同じ場所に置くこと）",bg="gray")
        entry_exe = tk.Entry(root,font=("Helvetica",10))
        label_arg = tk.Label(root,text="引数(空白区切り)",bg="white")
        entry_arg = tk.Entry(root,font=("Helvetica",10))

        # Place the widgets in the grid
        label_problem.grid(row=hensuu.static_num,column=0)
        entry_problem.grid(row=hensuu.static_num,column=1)
        label_cpp.grid(row=hensuu.static_num+1,column=0)
        entry_cpp.grid(row=hensuu.static_num+1,column=1)
        label_exe.grid(row=hensuu.static_num+2,column=0)
        entry_exe.grid(row=hensuu.static_num+2,column=1)
        label_arg.grid(row=hensuu.static_num+3,column=0)
        entry_arg.grid(row=hensuu.static_num+3,column=1)
        hensuu.static_num += 4
        entry_list.append([entry_cpp,entry_problem,entry_exe,entry_arg])
    text = tk.StringVar()
    text.set("フォームに記入")

    button = tk.Button(root,text="問題フォーム追加",command=lambda:make_form())
    button.grid(row=0,column=1)
    label = tk.Label(root,textvariable=text,bg="red")
    label.grid(row=0,column=0)
    extention_button = tk.Button(root,text="txtの作成",command=lambda:text.set(make_txtfile(entry_list)))
    extention_button.grid(row=0,column=2)
    make_form()
    root.mainloop()

def main():
    gui()

if __name__ == "__main__":
    main()
