#!/usr/bin/python

def fill(cake):
    r = len(cake)
    if r == 0:
        return cake
    c = len(cake[0])
    if c == 0:
        return cake
    chars = []
    for i in range(0,r):
        count = c
        for j in range(0,c):
            if cake[i][j] == '?':
                count -= 1
        chars.append(count)
    for i in range(0, r):
        if not chars[i] == 0:
            # begin to fill the blank on that line
            l = []
            for j in range(0,c):
                l.append(cake[i][j])
            j = 0
            while (l[j] == '?'):
                j += 1
            letter = l[j]
            for k in range(0,j):
                l[k] = letter
            while (j < len(l)):
                if l[j] == '?':
                    l[j] = letter
                    j += 1
                else:
                    letter = l[j]
                    j += 1
            l = ''.join(l)
            cake.pop(i)
            cake.insert(i, l)
            chars[i] == c
    # then fill in the 
    # print "inside function cake:"
    # print cake
    i = 0
    while (i < len(cake) and chars[i] == 0):
        i += 1
    if i == len(cake):
        return cake
    else:
        l = cake[i]
        #print "inside function cake:"
        #print cake
        for k in range(0,i):
            cake.pop(k)
            cake.insert(k, l)
        #print "inside function cake:"
        #print cake
        for k in range(i, len(cake)):
            if chars[k] == 0:
                cake.pop(k)
                cake.insert(k, l)
            else:
                l = cake[k]
    return cake

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0,t):
        s = raw_input()
        r, c = int(s.split()[0]), int(s.split()[1])
        cake = []
        for j in range(0,r):
            cake.append(raw_input())
        # now I have the cake
        cake = fill(cake)
        print "Case #" + str(i + 1) + ":"
        for j in range(0,r):
            print cake[j]
