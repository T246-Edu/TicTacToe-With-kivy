from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.animation import Animation
anim = Animation(x=50) + Animation(size=(80, 80), duration=1)
app = """
MDFloatLayout:
    md_bg_color:1,1,1,1
    MDGridLayout:
        cols:2
        size_hint:.5,.1
        pos_hint:{"center_x":.5,"center_y":.85}
        Button:
            id:userX
            text:"X"
            font_size:"40sp"
            on_release:app.select(userX)
        Button:
            id:userO
            text:"O"
            font_size:"40sp"
            on_release:app.select(userO)
    MDGridLayout:
        size_hint:.8,.5
        pos_hint:{"center_x":.5,"center_y":.5}
        cols:3
        rows:3
        Button:
            id:btn1
            background_color:1,.1,.5,.5
            color:1,1,1,1
            text:""
            font_size:"40sp"
            on_release:app.r(btn1)
        Button:
            id:btn2
            background_color:1,.1,.5,.5
            color:1,1,1,1
            text:""
            font_size:"40sp"
            on_release:app.r(btn2)
        Button:
            id:btn3
            background_color:1,.1,.5,.5
            color:1,1,1,1
            text:""
            font_size:"40sp"
            on_release:app.r(btn3)
        Button:
            id:btn4
            text:""
            background_color:1,.1,.5,.5
            color:1,1,1,1
            font_size:"40sp"
            on_release:app.r(btn4)
        Button:
            id:btn5
            background_color:1,.1,.5,.5
            color:1,1,1,1
            text:""
            font_size:"40sp"
            on_release:app.r(btn5)
        Button:
            id:btn6
            text:""
            font_size:"40sp"
            on_release:app.r(btn6)
            background_color:1,.1,.5,.5
            color:1,1,1,1
        Button:
            id:btn7
            text:""
            font_size:"40sp"
            on_release:app.r(btn7)
            background_color:1,.1,.5,.5
            color:1,1,1,1
        Button:
            id:btn8
            text:""
            font_size:"40sp"
            background_color:1,.1,.5,.5
            color:1,1,1,1
            on_release:app.r(btn8)
        Button:
            id:btn9
            background_color:1,.1,.5,.5
            color:1,1,1,1
            text:""
            font_size:"40sp"
            on_release:app.r(btn9)
    MDIconButton:
        icon:"restore"
        pos_hint:{"center_x":.5,"center_y":.08}
        user_font_size:"40sp"
        on_release:app.restart()
    MDLabel:
        id:result
        text:""
        halign:"center"
        pos_hint:{"center_x":.5,"center_y":.16}
        font_size:"30sp"
"""
class TicTacToe(MDApp):
    user = ""
    not_user = ""
    first_user = ""
    i = 0
    def build(self):
        return Builder.load_string(app)
    def select(self,user):
        if user.text == "X":
            self.root.ids.userO.disabled = True
            self.user = "X"
            self.not_user = "O"
            self.first_user="X"
        else:
            self.root.ids.userX.disabled = True
            self.user = "O"
            self.not_user = "X"
            self.first_user="O"
    def r(self,text):
        anim.start(text)
        if text.text == "" and self.user!="":
            if self.i%2 == 0:
                text.text = self.user
                if self.first_user == "X":
                    self.root.ids.userO.disabled = False
                    self.root.ids.userX.disabled = True
                elif self.first_user == "O":
                    self.root.ids.userX.disabled = False
                    self.root.ids.userO.disabled = True
            else:
                if self.first_user == "X":
                    self.root.ids.userO.disabled = True
                    self.root.ids.userX.disabled = False
                elif self.first_user == "O":
                    self.root.ids.userX.disabled = True
                    self.root.ids.userO.disabled = False
                text.text = self.not_user
            self.i+=1
        if self.user != "":
            if self.root.ids.btn1.text == self.user and self.root.ids.btn2.text == self.user and self.root.ids.btn3.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn4.text == self.user and self.root.ids.btn5.text == self.user and self.root.ids.btn6.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn7.text == self.user and self.root.ids.btn8.text == self.user and self.root.ids.btn9.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn1.text == self.user and self.root.ids.btn4.text == self.user and self.root.ids.btn7.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn2.text == self.user and self.root.ids.btn5.text == self.user and self.root.ids.btn8.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn3.text == self.user and self.root.ids.btn6.text == self.user and self.root.ids.btn9.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn1.text == self.user and self.root.ids.btn5.text == self.user and self.root.ids.btn9.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn3.text == self.user and self.root.ids.btn5.text == self.user and self.root.ids.btn7.text == self.user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn1.text == self.not_user and self.root.ids.btn2.text == self.not_user and self.root.ids.btn3.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn4.text == self.not_user and self.root.ids.btn5.text == self.not_user and self.root.ids.btn6.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn7.text == self.not_user and self.root.ids.btn8.text == self.not_user and self.root.ids.btn9.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn1.text == self.not_user and self.root.ids.btn4.text == self.not_user and self.root.ids.btn7.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn2.text == self.not_user and self.root.ids.btn5.text == self.not_user and self.root.ids.btn8.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn3.text == self.not_user and self.root.ids.btn6.text == self.not_user and self.root.ids.btn9.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn1.text == self.not_user and self.root.ids.btn5.text == self.not_user and self.root.ids.btn9.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
            elif self.root.ids.btn3.text == self.not_user and self.root.ids.btn5.text == self.not_user and self.root.ids.btn7.text == self.not_user:
                if self.root.ids.userO.disabled == False:
                    self.root.ids.result.text = "Player X Won"
                else:
                    self.root.ids.result.text = "Player O Won"
    def restart(self,restart=True):
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = "" 
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = "" 
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""
        self.user = ""
        self.not_user = ""
        self.root.ids.userX.disabled = False
        self.root.ids.userO.disabled = False
        self.i = 0
        if restart == True:
            self.root.ids.result.text  = ""
TicTacToe().run()