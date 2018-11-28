f_in = open('B-small-attempt0.in', 'r')
f_out = open('B.out', 'w')

from itertools import product
from math import pow

def supercount(s, sub):
    n1 = len(s)
    n2 = len(sub)
    k = 0
    for i in range(n1 - n2 + 1):
        if s[i:i + n2] == sub:
            k += 1
    return k

T = int(f_in.readline().strip())
for i in range(1, T + 1):
    K, L, S = map(int, f_in.readline().strip().split())
    k = f_in.readline().strip()
    l = f_in.readline().strip()

    if not set(l).issubset(k):
        y = 0.0
    else:
        p = product(k, repeat=S)
        good_words_count = []
        for x in p:
            t = ''.join(x)
            if l in t:
                k = supercount(t, l)
                good_words_count.append(k)
                #print(t, k) # debug

        ban_num = max(good_words_count)
        #print(ban_num) # debug

        good_words_count = [ban_num - j for j in good_words_count]
        #print(good_words_count) # debug

        y = (sum(good_words_count) + (pow(K, S) - len(good_words_count)) * ban_num) / pow(K, S)

    f_out.write('Case #' + str(i) + ': ' + str(y) + '\n')


f_out.close()
f_in.close()