# -*- coding: utf-8 -*-


def gen_shifts(num):
    length = len(str(num))
    seen = set()
    for i in range(1,length):
        shifted = (num % 10**i)*10**(length-i) + num // 10**i
        if shifted in seen:
            continue
        seen.add(shifted)
        yield shifted


with open('C-small-attempt0.in') as f, open ('out.txt','w') as f_out:
    f.__next__()

    for i,line in enumerate(f,1):
        line = line.rstrip()
        values = [int(el) for el in line.split()]
        A,B = values
        count = 0
        S = set()
        for n in range(A,B):
            for m in gen_shifts(n):
                if n < m and m <=B:
                    S.add((n,m))
                    count += 1


        out = 'Case #{}: {}\n'.format(i,count)
        #print(out)
        f_out.write(out)

        



