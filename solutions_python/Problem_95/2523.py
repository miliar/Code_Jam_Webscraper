# -*- coding: utf8 -*-

import string

class Googlerese(object):
    def __init__(self):
        """
        Build a translation table from the given examples.
        """
        fro = """ejp mysljylc kd kxveddknmc re jsicpdrysi
        rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
        de kr kd eoya kw aej tysr re ujdr lkgc jv qz"""
        to = """our language is impossible to understand
        there are twenty six factorial possibilities
        so it is okay if you want to just give up zq"""
        self.transTable = string.maketrans(fro, to)
        
    def translate(self, coded):
        return string.translate(coded, self.transTable)
        
def main():
    print "Ensure you are in the question folder and the folder is writable"
    rese = Googlerese()
    que = raw_input("enter the filename of the question: ")
    q = open(que, "r")
    q.readline() #omit the first line
    result = open("answer.txt", "w")
    t = 1
    for i in q:
        print "Case #{0}: {1}".format(t, rese.translate(i)),
        result.write("Case #{0}: {1}".format(t, rese.translate(i)))
        t += 1
    result.close()
    q.close()
    print "result successfully written to: answer.txt"

main()
