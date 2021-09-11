import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import numexpr
import pdb

class Handler:
    def __init__(self):
        #self.queue_draw()
        pass

    def pdb(self, button):
        import pdb; pdb.set_trace()

    def onDestroy(self, *args):
        Gtk.main_quit()

    def changeBar(self, *args):
        text = widthEntry.get_text()
        bar=builder.get_object("levelbar")
        if text == "":
            bar.set_value(0)
            setStars(0)
        try:
            bar.set_value(float(text))
            setStars(float(text))
        except ValueError: pass

    def calculate(self, *args):
        textbuffer = calc.get_buffer()
        text = textbuffer.get_text()
        print(text)

        try:
            result = str(int(numexpr.evaluate(text)))
        except:
            textbuffer.set_text("Error")
        else:
            textbuffer.set_text(result, len(result))
            widthEntry.set_text(result)
        calc.set_position(len(result))
        calc.grab_focus_without_selecting()

    def shutdown(self, button):
        import os
        os.system("pkexec shutdown now")

    '''
    def keyPressEvent(self, widget, event):
        if event.keyval == 106:
            import pdb; pdb.set_trace()
    '''

    def leave(self, widget, event):
        try:
            setStars(float(widthEntry.get_buffer().get_text()))
        except ValueError:
            pass

    def __getattr__(self, name, *args):
        if name.startswith("star"):
            number=name[4:]
            def onStarPressed(widget, event):
                if event.button == 1:
                    widthEntry.set_text(str(int(number)/2))
            return onStarPressed

        if name.startswith("enter"):
            number=name[5:]
            def onEnter(widget, event):
                setStars(int(number)/2)
            return onEnter

        return lambda *args: print({"name": name, "args": args})

builder = Gtk.Builder()
builder.add_from_file("test.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
button=builder.get_object("buttonid")
widthEntry=builder.get_object("widthEntry")
calc=builder.get_object("calc")

#builder.get_object("box").add(Gtk.Arrow())

hb = builder.get_object("headerBar")
hb.get_parent().remove(hb)
#builder.get_object("boxtest").add(hb)
window.set_titlebar(hb)

stars = []
for i in range(1,6):
    stars.append(builder.get_object("star" + str(i)))

def setStars(num):
    for i, star in enumerate(stars):
        if num<i+0.5:
            star.set_from_icon_name("non-starred-symbolic", Gtk.IconSize.DIALOG)
        elif num>=i+1:
            star.set_from_icon_name("starred-symbolic", Gtk.IconSize.DIALOG)
        else:
            star.set_from_icon_name("semi-starred-symbolic", Gtk.IconSize.DIALOG)
            
window.show_all()
calc.grab_focus_without_selecting()
#import pdb; pdb.set_trace()
Gtk.main()