import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import numexpr

class Handler:
    def __init__(self):
        '''
        self.set_titlebar(
            builder.get_object("levelbar")
        )
        '''
        pass

    def onDestroy(self, *args):
        Gtk.main_quit()

    def changeBar(self, *args):
        text = entry.get_text()
        if text == "":
            bar.set_value(0)
        try:
            bar.set_value(float(text))
        except ValueError: pass

    def popoverButtonPressed(self, button):
        print(1)
        popover.popup()

    def calculate(self, *args):
        textbuffer = builder.get_object("calc").get_buffer()
        text = textbuffer.get_text()
        print(text)

        try:
            result = str(int(numexpr.evaluate(text)))
        except:
            textbuffer.set_text("Error")
        else:
            textbuffer.set_text(result, len(result))

    '''
    def keyPressEvent(self, widget, event):
        if event.keyval == 106:
            import pdb; pdb.set_trace()
    '''

    def __getattr__(self, name, *args):
        return lambda *args: print({"name": name, "args": args})

builder = Gtk.Builder()
filename = "test.glade"
#filename = input("filename>")
builder.add_from_file(filename)
builder.connect_signals(Handler())

window = builder.get_object("window1")
button=builder.get_object("buttonid")
popover=builder.get_object("popover")
entry=builder.get_object("entryid")
bar=builder.get_object("levelbar")

box=builder.get_object("box")
arrow=Gtk.Arrow()
box.add(arrow)

'''
window.set_titlebar(
    builder.get_object("headerBar")
)
'''
window.show_all()
#import pdb; pdb.set_trace()
Gtk.main()