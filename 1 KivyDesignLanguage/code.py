import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):

	name = ObjectProperty(None)
	composer = ObjectProperty(None)
	piece = ObjectProperty(None)

	def press(self):
		name = self.name.text
		composer = self.composer.text
		piece = self.piece.text
		print(f'Hello {name}, you like {composer}, and your favourite piece is {piece}')
		# Add widget for information
		# self.add_widget(Label(text=f'Hello {name},you like {favComp}, and your favourite piece is {favPiece}'))
		# Adding widgets with this style is far more difficult
		# So we'll just use the print function

		# Clear the text input boxes
		self.name.text = ""
		self.composer.text = ""
		self.piece.text = ""

class  MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()
