from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from time import strftime
from kivy.clock import Clock


class Tela(MDLabel):
    def hora(self,*args):
        self.text = strftime("%H: %M: %S")
        self.font_size = "60sp"
        self.pos_hint = {"center_x":.85, "center_y": .5}

class Relogio(MDApp):
    def build(self):
        tela = Tela()
        Clock.schedule_interval(tela.hora,1)
        return tela

if __name__=="__main__":
    Relogio().run()
