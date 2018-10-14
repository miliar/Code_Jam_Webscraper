#!/usr/bin/env python

def main():
    s = "yhesocvxduiglbkrztnwjpfmaq"
    conv = { chr( 65 + s.index(aS) ).lower() : aS for aS in s }
    conv[" "] = " "
    conv[chr(10)] = chr(10)

    ip = open("C:\Users\suryak\Downloads\A-small-attempt1.in", "r")
    op = open("output.txt", "a")
    for num, eachLine in enumerate( ip.readlines()[1:] ):
        converted = ""
        for eachLetter in eachLine:
            converted += conv[eachLetter]
        op.write( "Case #%d: %s" %(num+1, converted) )


if __name__ == '__main__':
    main()
