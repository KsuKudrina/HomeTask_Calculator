import interface as ifc
import mathematics as mt
# import logbook as lb 


def button_click():
    a = ifc.get_value()
    str_ = ifc.get_operations()
    b = ifc.get_value()
    mt.init(a,b)
    result = mt.do_it(str_)
    ifc.get_logbook(result)
    # lb.get_logbook(a,b,str_)
    