counter = 0
def split_candy(l):
    s1 = 0
    s2 =0
    for a in l:
        s1 = a ^ s1
        s2 = a + s2
    if s1 == 0:
        return s2 - l[0]
    else:
        return 'NO'
    
with open("C-large.in","r") as f:
    r = []
    for line in f:
        counter = counter + 1
        if counter == 1 or counter % 2 == 0:
            continue
        else:
            candyweights = map(int, line.split())
            candyweights.sort()
            r.append(split_candy(candyweights))

with open('C-large.out','w') as f:
    counter = 0
    for a in r:
        counter = counter +1
        f.write('Case #{}: {}\n'.format(counter, a))