from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import User_check
data =User_check.test("select * from employee;")
#print(data)
while len(data) % 6 !=0:
    data.append(("","","","","",""))
p=0
class NextScreen(Screen):
    label1 = ObjectProperty()
    label2 = ObjectProperty()
    label3 = ObjectProperty()
    label4 = ObjectProperty()
    label5 = ObjectProperty()
    label6 = ObjectProperty()
    label7 = ObjectProperty()
    label8 = ObjectProperty()
    label9 = ObjectProperty()
    label10 = ObjectProperty()
    label11 = ObjectProperty()
    label12 = ObjectProperty()
    label13 = ObjectProperty()
    label14 = ObjectProperty()
    label15 = ObjectProperty()
    label16 = ObjectProperty()
    label17 = ObjectProperty()
    label18 = ObjectProperty()


    button1 = ObjectProperty()
    button2 = ObjectProperty()
    button3 = ObjectProperty()
    button4 = ObjectProperty()
    button5 = ObjectProperty()
    button6 = ObjectProperty()
    button7 = ObjectProperty()
    button8 = ObjectProperty()
    button9 = ObjectProperty()
    button10 = ObjectProperty()
    button11 = ObjectProperty()
    button12 = ObjectProperty()
    button13 = ObjectProperty()
    button14 = ObjectProperty()

    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)
        self.add_widget(Image(source='new3.png', allow_stretch=True))  # Use your next screen background image
        self.add_widget(Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                               on_press=self.switch_to_home_screen))

        self.place_button(0.2, 0.473, 'Details', 40, "button1")
        self.place_button(0.28, 0.473, 'Select100', 40, "button2")
        self.place_button(0.434, 0.473, 'Details', 40, "button3")
        self.place_button(0.514, 0.473, 'Select', 40, "button4")
        self.place_button(0.664, 0.473, 'Details', 40, "button5")
        self.place_button(0.744, 0.473, 'Select', 40, "button6")
        self.place_button(0.2, 0.186, 'Details', 40, "button7")
        self.place_button(0.28, 0.186, 'Select', 40, "button8")
        self.place_button(0.434, 0.186, 'Details', 40, "button9")
        self.place_button(0.514, 0.186, 'Select', 40, "button10")
        self.place_button(0.664, 0.186, 'Details', 40, "button11")
        self.place_button(0.744, 0.186, 'Select', 40, "button12")
        self.place_button(0.82, 0.2, 'next', 40, "button13")

        self.add_widget(self.create_label("%s" %(data[0+p][0]), 0.3, 0.63, font_size=50, widget=self.label1))
        self.add_widget(self.create_label("%s" %(data[0+p][1]), 0.3, 0.594, font_size=50, widget=self.label2))
        self.add_widget(self.create_label("%s" %(data[0+p][2]), 0.3, 0.558, font_size=50, widget=self.label3))
        self.add_widget(self.create_label("%s"%(data[1+p][0]), 0.53, 0.63, font_size=50, widget=self.label4))
        self.add_widget(self.create_label("%s"%(data[1+p][1]), 0.53, 0.594, font_size=50, widget=self.label5))
        self.add_widget(self.create_label("%s"%(data[1+p][2]), 0.53, 0.558, font_size=50, widget=self.label6))
        self.add_widget(self.create_label("%s"%(data[2+p][0]), 0.76, 0.63, font_size=50, widget=self.label7))
        self.add_widget(self.create_label("%s"%(data[2+p][1]), 0.76, 0.594, font_size=50, widget=self.label8))
        self.add_widget(self.create_label("%s"%(data[2+p][2]), 0.76, 0.558, font_size=50, widget=self.label9))
        self.add_widget(self.create_label("%s"%(data[3+p][0]), 0.3, 0.34, font_size=50, widget=self.label10))
        self.add_widget(self.create_label("%s"%(data[3+p][1]), 0.3, 0.302, font_size=50, widget=self.label11))
        self.add_widget(self.create_label("%s"%(data[3+p][2]), 0.3, 0.267, font_size=50, widget=self.label12))
        self.add_widget(self.create_label("%s"%(data[4+p][0]), 0.53, 0.34, font_size=50, widget=self.label13))
        self.add_widget(self.create_label("%s"%(data[4+p][1]), 0.53, 0.302, font_size=50, widget=self.label14))
        self.add_widget(self.create_label("%s"%(data[4+p][2]), 0.53, 0.267, font_size=50, widget=self.label15))
        self.add_widget(self.create_label("%s"%(data[5+p][0]), 0.76, 0.34, font_size=50, widget=self.label16))
        self.add_widget(self.create_label("%s"%(data[5+p][1]), 0.76, 0.302, font_size=50, widget=self.label17))
        self.add_widget(self.create_label("%s"%(data[5+p][2]), 0.76, 0.267, font_size=50, widget=self.label18))




    def create_label(self, message, x_rel, y_rel, font_size=20, halign='center', valign='middle', widget=None):
        label_pos_rel = {'center_x': x_rel, 'center_y': y_rel}
        label = Label(text=message, font_size=font_size, halign=halign, valign=valign, pos_hint=label_pos_rel,
                      color=(0, 0, 0, 1))
        label.bind(on_press=lambda instance: self.on_widget_press(instance, widget))
        return label

    def place_button(self, x, y, button_label, font_size, widget_name=None):
        if button_label == "next":
            button = Button(
                text=button_label,
                size_hint=(None, None),
                size=(667, 150),
                pos_hint={'x': x, 'y': y},
                font_size=font_size,
                background_color=(1, 1, 1, 0),
                background_normal='',
                color=(0, 0, 0, 1)
            )
            button.bind(on_release=lambda instance: self.on_widget_press(instance, 'button13'))
            self.add_widget(button)
        else:
            button = Button(text=button_label, size_hint=(None, None), size=(200, 50),
                            pos_hint={'x': x, 'y': y}, font_size=font_size, background_normal='bg_button.png',
                            color=(0, 0, 0, 1))

            button.bind(on_release=lambda instance: self.on_widget_press(instance, widget_name))
            setattr(self, widget_name, button)  # Set the attribute dynamically
            self.add_widget(button)

    def on_widget_press(self, instance, widget):
        if widget is not None:
            if widget == self.button12:
                self.manager.current = 'home_screen'
                # Do something for Button 12
            elif widget == self.button2:
                print("Button 2 pressed!")
                self.manager.current = 'home_screen'
                # Do something for Button 2

    def clear_widgets(self):
        # Clear all widgets from the screen
        for widget in self.children[:]:
            self.remove_widget(widget)
    def switch_to_home_screen(self, instance):
        # Switch to the "HomeScreen"
        self.manager.current = 'home_screen'
