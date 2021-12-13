from kivy.app import App

from kivy.core.window import Window

from kivy.metrics import dp

from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty

from kivy.clock import Clock

class MyCalc(BoxLayout):
    result = StringProperty("")

    base = ""
    op = ""

    @staticmethod
    def __remove_lz(op):
        if op != '':
            if op.find('.') == -1:
                return str(int(op))
            else:
                return str(float(op))
        else:
            return ''

    def __is_continue(self):
        if self.base == '' and self.op == '':  
            return False
        elif self.base != '' and self.op == '':
            if self.base[-1] == ')' or self.base[-1].isdigit():
                return True
            else :
                return False
        else:
            return True

    def one(self, instance):
        self.op = self.op + "1"
        self.result = self.base + self.op 
    def two(self):
        self.op = self.op + "2"
        self.result = self.base + self.op
    def three(self):
        self.op = self.op + "3"
        self.result = self.base + self.op
    def four(self):
        self.op = self.op + "4"
        self.result = self.base + self.op
    def five(self):
        self.op = self.op + "5"
        self.result = self.base + self.op
    def six(self):
        self.op = self.op + "6"
        self.result = self.base + self.op
    def seven(self):
        self.op = self.op + "7"
        self.result = self.base + self.op
    def eight(self):
        self.op = self.op + "8"
        self.result = self.base + self.op
    def nine(self):
        self.op = self.op + "9"
        self.result = self.base + self.op
    def zero(self):
        self.op = self.op + "0"
        self.result = self.base + self.op
    def point(self):
        if(self.op.find('.') == -1):
            self.op = self.op + "."
        self.result = self.base + self.op
    def left_bracket(self):
        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        if self.op == '' and self.base == '':
            self.base = "("
        elif self.base != '' and self.op == '':
            if self.base[-1] == ')' or self.base[-1].isdigit():
                self.base = self.base + "*("
            else :
                self.base = self.base + "("
        else : 
            self.base = self.base + self.op + "*("

        self.op = ''

        self.result = self.base
    def right_bracket(self):
        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        if self.op == '' and self.base == '':
            return
        elif self.base != '' and self.op == '':
            if self.base[-1] == '(':
                self.base = self.base + "0)"
            else :
                self.base = self.base + ")"
        else : 
            self.base = self.base + self.op + ")"

        self.op = ''

        self.result = self.base

    def backspace(self):
        if self.op != "":
            self.op = self.op[0:-1]
        elif self.base != "":
            self.base = self.base[0:-1]

        self.result =  self.base + self.op

    def clear(self):
        self.base = ""
        self.op = ""
        self.result = ""

    def plus(self):
        # return if nothing to do here
        if not self.__is_continue():
            return

        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        self.base = self.base + self.op + "+"
        self.op = ''

        self.result = self.base
    def minus(self):
        # return if nothing to do here
        if not self.__is_continue():
            return

        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        self.base = self.base + self.op + "-"
        self.op = ''

        self.result = self.base
    def mult(self):
        # return if nothing to do here
        if not self.__is_continue():
            return

        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        self.base = self.base + self.op + "*"
        self.op = ''

        self.result = self.base
    def div(self):
        # return if nothing to do here
        if not self.__is_continue():
            return

        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)

        self.base = self.base + self.op + "/"
        self.op = ''

        self.result = self.base
    def equals(self):
        # return if nothing to do here
        if not self.__is_continue():
            return

        if self.op == '.':
            self.op = '0'

        self.op = MyCalc.__remove_lz(self.op)
        try:
            self.base = str(eval(self.base + self.op))
        except ZeroDivisionError:
            self.base = ''
        except SyntaxError:
            self.base = ''
            
        self.op = ''

        self.result = self.base


class MyCalcApp(App):
    def build(self):
        return MyCalc(orientation = 'vertical')


if __name__ == '__main__':
    app = MyCalcApp()
    app.run()