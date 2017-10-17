#-*- coding: utf-8 -*-
conversion_factor = 0.62137119

print "Pozdravljeni, sem pretvornik kilometrov v milje."

while True:
    kilometri = int(raw_input("Prosimo vnesite število kilometrov, ki jih želite pretvoriti:"))
    milje = kilometri * conversion_factor
    print milje
    vprasanje = (raw_input("Želite opraviti novo pretvorbo? da/ne"))
    if vprasanje == "da":
        print "Ni problema."
    elif vprasanje == "ne":
        print "Nasvidenje!"
        break


