import sys
def pancake_flip(s,k):

    c = 0
    los = len(s)
    processing = True

    while processing:

        i = s.find('-')
        if i < 0: break

        if i + k <= los:
            if i + k == los: processing = False
            fs = flip(s[i:i+k])
            c += 1
            s = s[:i] + fs + s[i+k:los]
        else:
            processing = False
            return "IMPOSSIBLE"

    if checkFlipped(s):
        return c
    else:
        return "IMPOSSIBLE"

def flip(strn):
    s = ''
    for c in strn:
        if c == '-':
            s += '+'
        else:
            s += '-'
    return s

def checkFlipped(arr):
    return len(arr) == sum(c == '+' for c in arr)


if __name__ == '__main__':
    i = 0
    n = 0
    tc = 0
    inp = open('A-large.in.txt',"r")
    out = open('A-large.out.txt',"w")
    for line in inp:
        if i == 0:
            tc = int(line.strip())
        else:
            if i <= tc:
                vals = line.strip().split()
                s = vals[0].strip()
                k = int(vals[1].strip())
                ans = str(pancake_flip(s,k))
                s = str("Case #"+str(i)+": "+ans+"\n")
                out.write(s)
        i += 1
