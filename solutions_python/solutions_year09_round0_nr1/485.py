#!/usr/bin/python


def procesar(dic, case):
    sList = []

    mode = False
    tmp = set()

    for c in case:
        if c == '(':
            mode = True
            continue
        if c == ')':
            sList.append(tmp)
            tmp = set()
            mode = False
            continue
        tmp.add(c)
        if mode == False:
            sList.append(tmp)
            tmp = set()

    res = 0
    
    for palabra in dic:
        index = 0
        ok = True
        for c in palabra:
            if c not in sList[index]:
                ok = False
                break
            index += 1

        if ok:
            res += 1

    return res



if __name__ == "__main__":

    l,d,n = raw_input().split(' ')

    l = int(l)
    d = int(d)
    n = int(n)

    dic = set()

    for index in range(0, d):
        dic.add(raw_input())

    for index in range(1, n + 1):
        case = raw_input()
        res  = procesar(dic, case)

        print "Case #%s: %i"%(index, res)

