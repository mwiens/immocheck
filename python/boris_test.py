#!/usr/bin/python

import boris

if __name__ == "__main__":
    address = str(raw_input("Adresse für den Bodenrichtwert (z.B. Dresdner Straße 12B, 33813 Oerlinghausen:\n"))
    year = int(raw_input("Jahr für den Bodenrichtwert [2011 - 2016]:\n"))
    print address
    print year
    print "Bodenrichtwert für " + str(year) + ": " + boris.bodenrichtwert_by_address(address, year) + "€/qm \n"
