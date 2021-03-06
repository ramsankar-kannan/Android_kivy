from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class SignupScreen(BoxLayout):
    user_id = ObjectProperty(None)
    user_password = ObjectProperty(None)


class LoginScreen(GridLayout):
    role_voter = ObjectProperty(None)
    role_candidate = ObjectProperty(None)
    user_id = ObjectProperty(None)
    user_password = ObjectProperty(None)

    def on_login(self):
        if self.role_voter.state == "down":
            print("role:", self.role_voter.text)
        else:
            print("role:", self.role_candidate.text)
        print("username:", self.user_id.text)
        print("password:", self.user_password.text)


class TempApp(App):

    def build(self):
        return SignupScreen()


if __name__ == "__main__":
    Builder.load_file('core.kv')
    TempApp().run()
