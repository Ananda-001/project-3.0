from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import User_check
from details import Details
data =User_check.test("select * from employee;")
#print(data)
while len(data) % 6 !=0:
    data.append(("","","","","",""))
    done=True
global p,id
p=0
id=0
class NextScreen(Screen):

    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)
        self.add_widget(Image(source='new3.png', allow_stretch=True))  # Use your next screen background image
        self.add_widget(Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                               on_press=self.switch_to_home_screen))

        self.place_button(0.2, 0.473, 'Details', 40, "d1")
        self.place_button(0.28, 0.473, 'Select', 40, "s1")
        self.place_button(0.434, 0.473, 'Details', 40, "d2")
        self.place_button(0.514, 0.473, 'Select', 40, "s2")
        self.place_button(0.664, 0.473, 'Details', 40, "d3")
        self.place_button(0.744, 0.473, 'Select', 40, "s3")
        self.place_button(0.2, 0.186, 'Details', 40, "d4")
        self.place_button(0.28, 0.186, 'Select', 40, "s4")
        self.place_button(0.434, 0.186, 'Details', 40, "d5")
        self.place_button(0.514, 0.186, 'Select', 40, "s5")
        self.place_button(0.664, 0.186, 'Details', 40, "d6")
        self.place_button(0.744, 0.186, 'Select', 40, "s6")
        self.place_button(0.82, 0.2, 'next', 40, "nxt")
        self.place_button(0, 0.2, 'back', 40, "bk")

        self.add_widget(self.create_label("%s" %(data[0+p][0]), 0.3, 0.63,widget= "label1"))
        self.add_widget(self.create_label("%s" %(data[0+p][1]), 0.3, 0.594, widget="label2"))
        self.add_widget(self.create_label("%s" %(data[0+p][2]), 0.3, 0.558, widget="label3"))
        self.add_widget(self.create_label("%s"%(data[1+p][0]), 0.53, 0.63,widget= "label4"))
        self.add_widget(self.create_label("%s"%(data[1+p][1]), 0.53, 0.594,widget= "label5"))
        self.add_widget(self.create_label("%s"%(data[1+p][2]), 0.53, 0.558, widget="label6"))
        self.add_widget(self.create_label("%s"%(data[2+p][0]), 0.76, 0.63, widget="label7"))
        self.add_widget(self.create_label("%s"%(data[2+p][1]), 0.76, 0.594,widget= "label8"))
        self.add_widget(self.create_label("%s"%(data[2+p][2]), 0.76, 0.558,widget= "label9"))
        self.add_widget(self.create_label("%s"%(data[3+p][0]), 0.3, 0.34, widget="label10"))
        self.add_widget(self.create_label("%s"%(data[3+p][1]), 0.3, 0.302, widget="label11"))
        self.add_widget(self.create_label("%s"%(data[3+p][2]), 0.3, 0.267, widget="label12"))
        self.add_widget(self.create_label("%s"%(data[4+p][0]), 0.53, 0.34, widget="label13"))
        self.add_widget(self.create_label("%s"%(data[4+p][1]), 0.53, 0.302,widget="label14"))
        self.add_widget(self.create_label("%s"%(data[4+p][2]), 0.53, 0.267, widget="label15"))
        self.add_widget(self.create_label("%s"%(data[5+p][0]), 0.76, 0.34, widget="label16"))
        self.add_widget(self.create_label("%s"%(data[5+p][1]), 0.76, 0.302,widget= "label17"))
        self.add_widget(self.create_label("%s"%(data[5+p][2]), 0.76, 0.267, widget="label18"))




    def create_label(self, message, x_rel, y_rel, font_size=50, halign='center', valign='middle', widget=None):
        label_pos_rel = {'center_x': x_rel, 'center_y': y_rel}
        label = Label(text=message, font_size=font_size, halign=halign, valign=valign, pos_hint=label_pos_rel,
                      color=(0, 0, 0, 1))
        label.bind(on_press=lambda instance: self.on_widget_press(instance, widget))
        return label

    def place_button(self, x, y, button_label, font_size, widget_name):
        if button_label == "next" or button_label == "back":
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
            if button_label == "next":
                button.bind(on_release=lambda instance: self.on_widget_press(instance, 'nxt'))
                self.add_widget(button)
            else:
                button.bind(on_release=lambda instance: self.on_widget_press(instance, 'bk'))
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
            if widget == "nxt":
                 #self.manager.current = 'home_screen'
                self.manager.current= "next_screen"
                global p
                p+=6
                self.clear_labels()
                self.add_widget(self.create_label("%s" % (data[0 + p][0]), 0.3, 0.63, widget="label1"))
                self.add_widget(self.create_label("%s" % (data[0 + p][1]), 0.3, 0.594, widget="label2"))
                self.add_widget(self.create_label("%s" % (data[0 + p][2]), 0.3, 0.558, widget="label3"))
                self.add_widget(self.create_label("%s" % (data[1 + p][0]), 0.53, 0.63, widget="label4"))
                self.add_widget(self.create_label("%s" % (data[1 + p][1]), 0.53, 0.594, widget="label5"))
                self.add_widget(self.create_label("%s" % (data[1 + p][2]), 0.53, 0.558, widget="label6"))
                self.add_widget(self.create_label("%s" % (data[2 + p][0]), 0.76, 0.63, widget="label7"))
                self.add_widget(self.create_label("%s" % (data[2 + p][1]), 0.76, 0.594, widget="label8"))
                self.add_widget(self.create_label("%s" % (data[2 + p][2]), 0.76, 0.558, widget="label9"))
                self.add_widget(self.create_label("%s" % (data[3 + p][0]), 0.3, 0.34, widget="label10"))
                self.add_widget(self.create_label("%s" % (data[3 + p][1]), 0.3, 0.302, widget="label11"))
                self.add_widget(self.create_label("%s" % (data[3 + p][2]), 0.3, 0.267, widget="label12"))
                self.add_widget(self.create_label("%s" % (data[4 + p][0]), 0.53, 0.34, widget="label13"))
                self.add_widget(self.create_label("%s" % (data[4 + p][1]), 0.53, 0.302, widget="label14"))
                self.add_widget(self.create_label("%s" % (data[4 + p][2]), 0.53, 0.267, widget="label15"))
                self.add_widget(self.create_label("%s" % (data[5 + p][0]), 0.76, 0.34, widget="label16"))
                self.add_widget(self.create_label("%s" % (data[5 + p][1]), 0.76, 0.302, widget="label17"))
                self.add_widget(self.create_label("%s" % (data[5 + p][2]), 0.76, 0.267, widget="label18"))
                self.add_widget(
                    Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                           on_press=self.switch_to_home_screen))

                self.place_button(0.2, 0.473, 'Details', 40, "d1")
                self.place_button(0.28, 0.473, 'Select', 40, "s1")
                self.place_button(0.434, 0.473, 'Details', 40, "d2")
                self.place_button(0.514, 0.473, 'Select', 40, "s2")
                self.place_button(0.664, 0.473, 'Details', 40, "d3")
                self.place_button(0.744, 0.473, 'Select', 40, "s3")
                self.place_button(0.2, 0.186, 'Details', 40, "d4")
                self.place_button(0.28, 0.186, 'Select', 40, "s4")
                self.place_button(0.434, 0.186, 'Details', 40, "d5")
                self.place_button(0.514, 0.186, 'Select', 40, "s5")
                self.place_button(0.664, 0.186, 'Details', 40, "d6")
                self.place_button(0.744, 0.186, 'Select', 40, "s6")
                self.place_button(0, 0.2, 'back', 40, "bk")
                if done == False:
                    self.place_button(0.82, 0.2, 'next', 40, "nxt")
                # Do something for Button 12
        if widget in ["d1","d2","d3","d4","d5","d6"]:

            id =data[0 + p][1]
            details = Details(name='details')
            self.manager.add_widget(details)
            self.manager.current = "details"


        if widget == "bk" :
            # self.manager.current = 'home_screen'
            self.manager.current = "next_screen"
            p -= 6
            self.clear_labels()
            self.add_widget(self.create_label("%s" % (data[0 + p][0]), 0.3, 0.63, widget="label1"))
            self.add_widget(self.create_label("%s" % (data[0 + p][1]), 0.3, 0.594, widget="label2"))
            self.add_widget(self.create_label("%s" % (data[0 + p][2]), 0.3, 0.558, widget="label3"))
            self.add_widget(self.create_label("%s" % (data[1 + p][0]), 0.53, 0.63, widget="label4"))
            self.add_widget(self.create_label("%s" % (data[1 + p][1]), 0.53, 0.594, widget="label5"))
            self.add_widget(self.create_label("%s" % (data[1 + p][2]), 0.53, 0.558, widget="label6"))
            self.add_widget(self.create_label("%s" % (data[2 + p][0]), 0.76, 0.63, widget="label7"))
            self.add_widget(self.create_label("%s" % (data[2 + p][1]), 0.76, 0.594, widget="label8"))
            self.add_widget(self.create_label("%s" % (data[2 + p][2]), 0.76, 0.558, widget="label9"))
            self.add_widget(self.create_label("%s" % (data[3 + p][0]), 0.3, 0.34, widget="label10"))
            self.add_widget(self.create_label("%s" % (data[3 + p][1]), 0.3, 0.302, widget="label11"))
            self.add_widget(self.create_label("%s" % (data[3 + p][2]), 0.3, 0.267, widget="label12"))
            self.add_widget(self.create_label("%s" % (data[4 + p][0]), 0.53, 0.34, widget="label13"))
            self.add_widget(self.create_label("%s" % (data[4 + p][1]), 0.53, 0.302, widget="label14"))
            self.add_widget(self.create_label("%s" % (data[4 + p][2]), 0.53, 0.267, widget="label15"))
            self.add_widget(self.create_label("%s" % (data[5 + p][0]), 0.76, 0.34, widget="label16"))
            self.add_widget(self.create_label("%s" % (data[5 + p][1]), 0.76, 0.302, widget="label17"))
            self.add_widget(self.create_label("%s" % (data[5 + p][2]), 0.76, 0.267, widget="label18"))
            self.add_widget(
                Button(text='Go to Home Screen', size=(400, 100), size_hint=(None, None), pos=(300, 200),
                       on_press=self.switch_to_home_screen))

            self.place_button(0.2, 0.473, 'Details', 40, "d1")
            self.place_button(0.28, 0.473, 'Select', 40, "s1")
            self.place_button(0.434, 0.473, 'Details', 40, "d2")
            self.place_button(0.514, 0.473, 'Select', 40, "s2")
            self.place_button(0.664, 0.473, 'Details', 40, "d3")
            self.place_button(0.744, 0.473, 'Select', 40, "s3")
            self.place_button(0.2, 0.186, 'Details', 40, "d4")
            self.place_button(0.28, 0.186, 'Select', 40, "s4")
            self.place_button(0.434, 0.186, 'Details', 40, "d5")
            self.place_button(0.514, 0.186, 'Select', 40, "s5")
            self.place_button(0.664, 0.186, 'Details', 40, "d6")
            self.place_button(0.744, 0.186, 'Select', 40, "s6")
            self.place_button(0, 0.2, 'back', 40, "bk")
            self.place_button(0.82, 0.2, 'next', 40, "nxt")

    def clear_widgets(self):
        # Clear all widgets from the screen
        for widget in self.children[:]:
            if widget == Image:

                pass
            else:
                self.remove_widget(widget)

    def clear_labels(self):
        # Clear only label widgets from the screen
        widgets_to_remove = [widget for widget in self.children if isinstance(widget, Label)]
        for widget in widgets_to_remove:
            self.remove_widget(widget)
    def switch_to_home_screen(self, instance):
        # Switch to the "HomeScreen"
        self.manager.current = 'home_screen'
