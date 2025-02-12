from tkinter import *
from tkinter import messagebox as m
from PIL import Image as img


def png_to_ico(a: str, b: str):
    a = str(a)
    b = str(b + ".ico")
    image = img.open(a)  # 核心代码
    image.save(b, format="ICO")
    m.showinfo("完成", "已在名下目录生成ico文件")


class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""

    def __init__(self):
        """构造函数"""

        super().__init__()

        self.title('png转图标工具')
        self.resizable(False, False)
        self.iconbitmap('png_ico.ico')
        self.init_ui()

    def init_ui(self):
        """初始化界面"""

        account, passwd = StringVar(), StringVar()
        account.set('')
        passwd.set('')

        group = LabelFrame(self, text="转化", padx=5, pady=5)
        group.pack(padx=20, pady=10)

        f1 = Frame(group)
        f1.pack(padx=5, pady=5)
        Label(f1, text='png路径：').pack(side=LEFT, pady=5)
        Entry(f1, textvariable=account, width=15, justify=CENTER).pack(side=LEFT, pady=5)

        f2 = Frame(group)
        f2.pack(padx=5, pady=5)
        Label(f2, text='ico名称(不可输入扩展名)：').pack(side=LEFT, pady=5)
        Entry(f2, textvariable=passwd, width=15, justify=CENTER).pack(side=LEFT, pady=5)

        btn = Button(self, text='转换', bg='#FFFFFF', command=lambda: png_to_ico(account.get(), passwd.get()))
        btn.pack(fill=X, padx=20, pady=10)


# 运行
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
