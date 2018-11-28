import math

def main():
    """
        docstring for main
    """
    exit_values = []
    N = int(raw_input())
    for case in range(1,N+1):
        rang = raw_input()
        rang = rang.split()
        Inf = int(rang[0])
        Sup = int(rang[1])
        inf = int(math.sqrt(Inf))
        sup = int(math.sqrt(Sup))
        value = 0
        for num in range(inf,sup+1):
            nn = num*num
            if is_fair(num) and is_fair(nn) and (Inf <= nn <= Sup):
                value +=1
        exit_values.append((case,value))

    for value in exit_values:
        print "Case #%d: %d" % (value[0], value[1])

def is_fair(n):
    if n-10 < 0:
        return True
    if all_same(list(str(n))):
        return True
    d = str(n)
    le = len(d)
    res = True
    for i in range(0,le/2):
        if d[i] != d[le-i-1]:
            res = False
    return res

def all_same(items):
    return all(x == items[0] for x in items)

if __name__ == '__main__':
    main()
