from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.widget import Widget          # Нужно для пустых виджетов
from kivy.uix.label import Label            # Нужно для Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

from bluetooth import discover_devices
#from pyautogui import *


#Config.set('graphics', 'resizable', 0)  # Размер окна будет неизменяемый
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def build(self):    #Обязательно нужно создать метод build

        # Scanning for bluetooth devices
        #devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
        devices = discover_devices(lookup_names = True, lookup_class = True)
        number_of_devices = len(devices)
        nd = str(number_of_devices) + '***'
##        nd = '22222'

##        #print(number_of_devices,"devices found")
##        label = Label(text=str(number_of_devices) + " devices found")



        #self.formula = "0"

        bl = BoxLayout(orientation = 'vertical', padding = 25)
        self.lbl = Label(text=nd, font_size = 20,
                            halign = "right",
                            valign = "center",
                            size_hint = (1,.3),                      # Ширину Label делаем 100%, высоту - 30%
                            text_size = (400-50, 500 * .3 - 50))     # Размер текстуры делаем равным размеру виджета
        
        bl.add_widget(self.lbl)
        
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .7))         # Ширину GridLayout делаем 100%, высоту - 70%

        gl.add_widget(Button(text = "7", on_press = self.add_number))
        gl.add_widget(Button(text = "8", on_press = self.add_number))
        gl.add_widget(Button(text = "9", on_press = self.add_number))
        gl.add_widget(Button(text = "*", on_press = self.add_number))

        gl.add_widget(Button(text = "4", on_press = self.add_number))
        gl.add_widget(Button(text = "5", on_press = self.add_number))
        gl.add_widget(Button(text = "6", on_press = self.add_number))
        gl.add_widget(Button(text = "-", on_press = self.add_number))

        gl.add_widget(Button(text = "1", on_press = self.add_number))
        gl.add_widget(Button(text = "2", on_press = self.add_number))
        gl.add_widget(Button(text = "3", on_press = self.add_number))
        gl.add_widget(Button(text = "+", on_press = self.add_number))

        #gl.add_widget(Widget())                                        #пустой виджет
        gl.add_widget(Button(text = "С", on_press = self.clear))
        gl.add_widget(Button(text = "0", on_press = self.add_number))
        gl.add_widget(Button(text = ".", on_press = self.add_number))
        gl.add_widget(Button(text = "=", on_press = self.calc))

        bl.add_widget(gl)

        return bl

    def add_number(self, instance):
        pass
##        if (self.lbl.text == "0"):
##            self.lbl.text = instance.text
##        else:
##            self.lbl.text += instance.text          # почему-то label не ообновляется, а пишется поверху

    def calc(self,instance):
        pass
##        self.lbl.text = str(eval(self.lbl.text))

    def clear(self,instance):
        pass
##        self.lbl.text = "0"
        
        



    #def add_operation(self, instance):
    #    self.formula += str(instance.text)
    #    self.update_label()

    #def update_label(self):
    #    #self.lbl.text = ""
    #    self.lbl.text = self.formula



if __name__ == "__main__":
   CalculatorApp().run()
    




























##        for addr, name, device_class in devices:
##
##            print("\n")
##
##            print("Device:")
##
##            print("Device Name: %s" % (name))
##
##            print("Device MAC Address: %s" % (addr))
##
##            print("Device Class: %s" % (device_class))
##
##            print("\n")
##
##
##
##
##        return bl







if __name__ == "__main__":
   CalculatorApp().run()
    
