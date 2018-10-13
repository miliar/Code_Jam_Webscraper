#!/usr/bin/python

def translate(s):
    t = s.maketrans("yeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc\
            rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re\
            ujdr lkgc jvz","aoz our language is impossible to understand there are\
            twenty six factorial possibilities so it is okay if you want to\
            just give upq")
    return s.translate(t)

def main():
    fin = open("input.txt")
    fout = open("output.txt", 'w')
    i = 0
    for line in fin:
        if i == 0:
            pass
        else:
            fout.write("Case #%i: " % i)
            fout.write(translate(line))
        i+=1

main()
