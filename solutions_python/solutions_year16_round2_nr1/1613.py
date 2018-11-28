#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()

    

    def solve(cipher):
        cipher = list(cipher)
        collection = ""
        while "Z" in cipher :
            cipher.remove("Z")
            cipher.remove("E")
            cipher.remove("R")
            cipher.remove("O")
            collection = collection + "0"
        while "G" in cipher:
            cipher.remove("E")
            cipher.remove("I")
            cipher.remove("G")
            cipher.remove("H")
            cipher.remove("T")
            collection = collection + "8"
        while "W" in cipher :
            cipher.remove("T")
            cipher.remove("W")
            cipher.remove("O")
            collection = collection + "2"
        while "X" in cipher:
            cipher.remove("S")
            cipher.remove("I")
            cipher.remove("X")
            collection = collection + "6"

        while "S" in cipher:
            cipher.remove("S")
            cipher.remove("E")
            cipher.remove("V")
            cipher.remove("E")
            cipher.remove("N")
            collection = collection + "7"
        while "V" in cipher:
            cipher.remove("F")
            cipher.remove("I")
            cipher.remove("V")
            cipher.remove("E")
            collection += "5"
        while "U" in cipher:
            cipher.remove("F")
            cipher.remove("O")
            cipher.remove("U")
            cipher.remove("R")
            collection = collection + "4"



        while "O"  in cipher :
            cipher.remove("O")
            cipher.remove("N")
            cipher.remove("E")
            collection = collection + "1"



        while "N" in cipher:
            cipher.remove("N")
            cipher.remove("I")
            cipher.remove("N")
            cipher.remove("E")
            collection = collection + "9"

        while "H" in cipher:
            cipher.remove("T")
            cipher.remove("H")
            cipher.remove("R")
            cipher.remove("E")
            cipher.remove("E")
            collection += "3"


        #find inf
        collection = ''.join(sorted(collection))

        return collection



        
            


     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))

    
