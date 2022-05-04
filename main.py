# Derivatives Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from sympy import Limit, Symbol, S, diff, integrate, solve
import math

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-Mathematics"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"  
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Derivatives Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"   
                
""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
                    
            Button:
                font_size: '20sp'
                background_color: 0, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Derivatives Calculator"
                on_release:
                    app.root.current = "Derivatives"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
                
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Derivatives Calculators v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#Derivatives Calculator
Builder.load_string("""
<Derivatives>
    id:Derivatives
    name:"Derivatives"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Derivatives Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        value.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to derive"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10            
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
            TextInput:
                id: value
                text: value.text
                hint_text: "Respect = Value"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10  
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Derivative"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        Derivatives.derive(entry.text + "&" + prime.text + "$" + respect.text + "%" + value.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Derivatives(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Derivatives, self).__init__(**kwargs)
            
    layouts = []
    def derive(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("DERIVATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            percent_sign = entry.find("%")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:percent_sign]
            print("respect:",respect)
            
            value = entry[percent_sign+1:]
            print("value:",value)
            if value == "":
                value = "Nothing"
            
            if respect == "x":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            elif respect == "y":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            elif respect == "z":
                respect = Symbol(respect)
                print("Respect officially:",respect)
            else:
                print("Invalid Respect Input" )
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + str(respect) + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("+"," + ").replace("-"," - ").replace("***","**") ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Derive " + str(prime) + " time(s) with respect to " + str(respect),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                i = 0 #     2sin(2x)^2+3x^3+e^x-2ln(3x)
                while i < int(prime):
                    
                    print("Starting",i+1,"derivative")
                    func = func.replace("**","^").replace("*","")
                    print("func:",func)
                    func = str(func).replace(" ","").replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                    func = func.replace("-*x","-1*x").replace("-*y","-1*y").replace("-*z","-1*z")
                    func = func.replace("+*x","+1*x").replace("+*y","+1*y").replace("+*z","+1*z")
                    func = func.replace("(*x","(1*x").replace("(*y","(1*y").replace("(*z","(1*z")
                    func = func.replace("(-*x","(-1*x").replace("(-*y","(-1*y").replace("(-*z","(-1*z")
                    func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                    func = func.replace("ln","*ln").replace("log","*log")
                    func = func.replace("e**","*e**").replace("(*e**","(e**")
                    func = func.replace("+-","-").replace("-+","-")
                    func = func.replace("-*","-1*").replace("+*","+1*").replace("/*","/")
                    func = func.replace("***","**")
                    print("func filtered:",func)
                    
                    if func[0] == "*":
                        func = "1" + func
                        print("func fixed, * = [0]:",func)
                    print("func = ",func)
                    print("func data type",type(func))

                    func = str(diff(func,str(respect)))
                    print("Answer:",func)

                    print()
                    func_display_list = str(func).strip().split(" ")
                    print("func_display_list",func_display_list)
                    
                    if len(func_display_list) > 5 and len(func_display_list) < 12:
                        print("IF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_back_slice = str(func_display_list[5:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func_display_front_slice).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    elif len(func_display_list) > 12:
                        print("ELIF")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        func_display_front_slice = str(func_display_list[:5]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_front_slice",func_display_front_slice)
                        
                        func_display_mid_slice = str(func_display_list[5:11]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_mid_slice",func_display_mid_slice)
                        
                        func_display_back_slice = str(func_display_list[11:]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print("func_display_back_slice",func_display_back_slice)
                        
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func_display_front_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_mid_slice).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(func_display_back_slice).replace("**","^") ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    else:
                        print("ELSE")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("func_display_list",func_display_list)
                        self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i+1) + "(" + str(respect) + ") = " + str(func).replace("**","^"),font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    print("Completed",i+1,"derivative")
                    print("_________________________________________")
                    i = i + 1
                    
            if value != "Nothing":
                print("func = ",func)
                
                func = str(func).replace(str(respect),str(value)).replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","math.csc").replace("sec","math.sec").replace("cot","math.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","math.sec").replace("math.smath.secc","math.sec")
                print("func replaced x = ",func)
                
                func_evaled = eval(str(func))
                print("func_evaled = ",func_evaled)
                
                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "f" + "'" * (i) + "(" + value + ") = " + str(func_evaled),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif str(respect) == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Derivatives(name="Derivatives"))     
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class Derivatives_Calculator(App):
    def __init__(self, **kwargs):
        super(Derivatives_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Derivatives_Calculator().run()
