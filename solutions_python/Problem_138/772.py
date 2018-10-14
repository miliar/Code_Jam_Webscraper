def read_mapped(func=lambda x:x):
    return map(func, raw_input().split(" "))
def read_array(N, func):
    l = []
    for i in range(N):
        l.append(func(raw_input()))
    return l
def read_int():
    return int(raw_input())
def read_str():
    return raw_input()
def read_float():
    return float(raw_input())

T = read_int()

for case in range(T):
    n = read_int()
    naomi = read_mapped(float)
    ken = read_mapped(float)
    naomid = naomi[:]
    kend = ken[:]
    dwar, war = 0, 0
    for i in range(n):
        # Deceitful play here
        maxkend = max(kend)
        maxnaomid = max(naomid)
        minnaomid = min(naomid)
        if maxnaomid<maxkend:
            kend.remove(maxkend)
            naomid.remove(minnaomid)
        elif maxkend<maxnaomid:
            somevar = 0
            for x in naomid:
                if  x>maxkend:
                    somevar = x
                    break
            kend.remove(maxkend)
            naomid.remove(somevar)
            dwar += 1
        elif maxkend==maxnaomid:
            kend.remove(maxkend)
            naomid.remove(minnaomid)

        # Fair play here
        naomi_ = max(naomi)
        maxken = max(ken)
        minken = min(ken)
        if naomi_>maxken:
            ken.remove(minken)
            naomi.remove(naomi_)
            war += 1
        elif naomi_<maxken:
            somevar = 0
            for x in ken:
                if x>naomi_:
                    somevar = x
                    break
            ken.remove(somevar)
            naomi.remove(naomi_)
        elif naomi_==maxken:
            ken.remove(minken)
            naomi.remove(naomi_)

    print "Case #{}: {} {}".format(case+1, dwar, war)

