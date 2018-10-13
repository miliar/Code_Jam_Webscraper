import sys

def tidy_numbers(n):

    strn = str(n)
    lon = len(strn)
    i = lon - 2
    s = ""
    while i >= 0:
        if strn[i+1] < strn[i]:
            t = int(strn[i+1:]) + 1
            n -= t
            strn = str(n)
            if checkTidy(strn):
                return n
        else:
            i -= 1
    return n

def checkTidy(strn):

    if len(strn) <= 1: return True

    for i in range(1,len(strn)):
        if strn[i] < strn[i - 1]:
            return False
    return True


if __name__ == '__main__':
    i = 0
    n = 0
    m = 0
    inp = open('B-large.in.txt',"r")
    out = open('B-large-attempt0.out.txt',"w")
    for line in inp:
        n = int(line.strip())
        if i == 0:
            m = n
        else:
            if i <= m:
                s = str("Case #"+str(i)+": "+str(tidy_numbers(n))+"\n")
                out.write(s)
        i += 1
