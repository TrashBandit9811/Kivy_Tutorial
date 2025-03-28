from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('bg.kv')

class MyLayout(Widget):
	pass

class  MyApp(App):
	def build(self):
		Window.clearcolor = (0,0,0,1)
		return MyLayout()

if __name__ == '__main__':
	MyApp().run()
