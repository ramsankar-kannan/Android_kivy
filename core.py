import kivy

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty


class LoginScreen(GridLayout):
    user_id = ObjectProperty(None)
    user_password = ObjectProperty(None)

    def on_login(self):
        print("username:", self.user_id.text)
        print("password:", self.user_password.text)


class TempApp(App):

    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    Builder.load_file('core.kv')
    TempApp().run()
