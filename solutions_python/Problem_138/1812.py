__author__ = 'nguyensontung1404'

def eliminate(_list):
    if "\n" in _list[-1]:
        _list[-1] = _list[-1][:-1]
    return _list

def find(_list, number):
    for n in _list:
        if n > number:
            return n
    return None

def delete(naomi, ken):
    if len(naomi) == 0:
        return
    re = find(ken, naomi[0])
    if re == None:
        return
    else:
        del naomi[0]
        ken.remove(re)
        return delete(naomi, ken)

def delete2(naomi, ken):
    k = ken[:]
    for b in k:
        re = find(naomi, b)
        if re != None:
            ken.remove(b)
            naomi.remove(re)

def find_wScore(naomi, ken):
    delete(naomi, ken)
    return len(naomi)

def find_dScore(naomi, ken):
    global N
    delete2(naomi, ken)
    score = N - len(naomi)
    return score

def check(naomi, ken):
    for i in range(len(naomi)):
        if naomi[i] < ken[i]:
            return False
        return True

if __name__ == "__main__":
    import sys
    sys.stdin = open("D-small-attempt4.in")
    sys.stdout = open("output4.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        N = int(sys.stdin.readline())
        _str = eliminate(sys.stdin.readline().split(" "))
        naomi = sorted(map(float, _str))
        _str = eliminate(sys.stdin.readline().split(" "))
        ken =  sorted(map(float, _str))
        n1 = naomi[:]
        k1 = ken[:]
        n2 = naomi[:]
        k2 = ken[:]
        print "Case #%d:" %case, find_dScore(n1, k1), find_wScore(n2, k2)
