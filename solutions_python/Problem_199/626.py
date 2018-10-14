'''
aditya76
'''
T = int(raw_input())
def flip(meracake, stt, lgth):
    for idx in  range(stt, stt + lgth):
        if meracake[idx] == '+':
            meracake[idx] = '-'
        else:
            meracake[idx] = '+'

for t in xrange(1, T + 1):
    mystr = raw_input()
    meracake, lgth = mystr.split(' ')[0], int(mystr.split(' ')[1])
    meracake = [i for i in meracake]
    idx = 0
    res   = 0
    length = len(meracake)
    for i in meracake:
        if idx + lgth > length:
            if '-' in meracake:
                res = 'IMPOSSIBLE'
                break
        else:
            if i == '+':
                pass
            else:
                res += 1
                flip(meracake, idx, lgth)
        idx += 1
    print "Case #{}: {}".format(t, res)
