
if __name__ == "__main__":
    T = 0
    lettdict = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v',
                'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b',
                'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j',
                'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
    lst = []
    f = open("GCJ2012_A_IN.txt", "r")
    try:
        lst = []
        for line in f:
            if T == 0:
                T = int(line.strip()) + 1
            elif T == 1:
                break
            else:
                T = T - 1
                s = line.strip()
                s2 = ''
                for c in s:
                    if c in lettdict:
                        s2 = s2 + lettdict[c]
                    else:
                        s2 = s2 + c
                lst.append(s2)
    finally:
        f.close()

    f = open("GCJ2012_A_OUT.txt", "w")
    try:
        for i in range(len(lst)):
            f.write('Case #' + str(i + 1) + ': ' + lst[i])
            if i < len(lst) - 1:
                f.write('\n')
    finally:
        f.close()
