#in_file = open('a.in')
in_file = open('//Users/simple/Desktop/A-large.in')
T = int(in_file.readline())
for i in range(T):
    chars = {}
    orig = in_file.readline().strip();
    r_v = {}
    r_v[orig[0]] = 1
    v = 0
    for c in orig:
        if c not in r_v.keys():
            r_v[c] = v
            if v ==0:
                v = 2
            else:
                v += 1
    l = len(orig) -1
    r = len(r_v)
    if len(r_v) == 1 :
        r_v[list(r_v.keys())[0]] = 1
        r = 2
    result = 0
    for c in orig:
        #print(r,c,l,r_v[c] * (r**l))
        result += r_v[c] * (r**l)
        l -= 1
    #print(r_v)
    print('Case #{}: {}'.format(i+1, result))

