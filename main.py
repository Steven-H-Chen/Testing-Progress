from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Builder.load_file("container.kv")

class passer(FloatLayout):
    pass

class Tpro(App):
    def build(self):
        img = Image(source='path_to_your_image.png')
        return 
    
    
if __name__ == '__main__':
    Tpro().run()