#! /usr/bin/env python
import sys



# parsing input

def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]




# computation

def process(line):
    tab = line.split()
    return int(tab[0]),int(tab[1])


def algo(n,k):
    m = 2 ** n
    res = k % m
    return (res == m-1)


def msg(n,k,t):
    format = "Case #%d: %s\n"
    if algo(n,k):
        str = "ON"
    else :
        str = "OFF"
    return format % (t, str)


# writing output


# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
#    print "programme appele %s" % input
    f = open(input,'r')
    l=f.readline()
    t = int(l[0])
    o = open(output,'w')
 #   print "nb de lignes : %d"%t
    c = 1
    for line in f:
  #      print "ligne %d"%c
        n,k = process(line)
   #     print "%d %d"% (n,k)
        oline = msg(n,k,c)
    #    print oline
        c+=1
        o.write(oline)
    o.close()
