import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):

	#Initialize infinite keywords
	def __init__(self, **kwargs):
		# Call grid layout constructor
		super(MyGridLayout, self).__init__(**kwargs)
		
		# Set columns
		self.cols = 2
		self.row_force_default=True
		self.row_default_height=120
		self.col_force_default=True
		self.col_default_width=200

		# Create a second gridlayout
		self.top_grid = GridLayout(
			row_force_default=True,
			row_default_height=40,
			col_force_default=True,
			col_default_width=200
			)
		# Set number of columns in our new top grid
		self.top_grid.cols = 2


		# NAME
		# Add widgets
		self.top_grid.add_widget(Label(text="Name: "))

		# Add Input Box
		self.name = TextInput(multiline=False)
		self.top_grid.add_widget(self.name)

		# FAVORITE COMPOSER
		# Add widgets
		self.top_grid.add_widget(Label(text="Favorite Composer: "))
		# Add Input Box
		self.favComp = TextInput(multiline=False)
		self.top_grid.add_widget(self.favComp)

		# FAVORITE PIECE BY THEM
		# Add widgets
		self.top_grid.add_widget(Label(text="Favorite Piece: "))
		# Add Input Box
		self.favPiece = TextInput(multiline=False)
		self.top_grid.add_widget(self.favPiece)

		# Add top layout to app
		self.add_widget(self.top_grid)


		# Create submit button
		self.submit = Button(text="Submit",
		font_size=32,
		size_hint_y=None,
		height=50,
		size_hint_x=None,
		width=200)

		# Bind the button
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)
		
	
	def press(self, instance):
		name = self.name.text
		favComp = self.favComp.text
		favPiece = self.favPiece.text
		print(f'Hello {name},you like {favComp}, and your favourite piece is {favPiece}')
		# Add widget for information
		self.add_widget(Label(text=f'Hello {name},you like {favComp}, and your favourite piece is {favPiece}'))
		# Clear the text input boxes
		self.name.text = ""
		self.favComp.text = ""
		self.favPiece.text = ""

class  MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()
