import gi
import numexpr

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def equalsPressed(self, button):
        print(1)

        textbuffer = textView.get_buffer()
        start_iter = textbuffer.get_start_iter()
        end_iter = textbuffer.get_end_iter()
        text = textbuffer.get_text(start_iter, end_iter, True)
        print(text)

        try:
            result = int(numexpr.evaluate(text))
        except:
            textbuffer.set_text("Error")
        else:
            textbuffer.set_text(str(result))

    def __getattr__(self, *args):
        print(args)

builder = Gtk.Builder()
builder.add_from_file("calc.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")

textView=builder.get_object("textView")
textbuffer = textView.get_buffer()

window.show_all()
#import pdb; pdb.set_trace()
Gtk.main()


'''
start_iter = textbuffer.get_start_iter()
end_iter = textbuffer.get_end_iter()
text = textbuffer.get_text(start_iter, end_iter, True)  

'''