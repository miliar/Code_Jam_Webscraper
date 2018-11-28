def tidy(n):
    rn = list(map(int, n[::-1]))
    l = 0
    for i in range(len(rn[:-1])):
        if (rn[i] < rn[i+1]):
            l = i + 1
            rn[i+1] -= 1

    a = rn[::-1]
    b = a[:-l or None]
    b.extend(l * [9])
    return ''.join(str(x) for x in b).lstrip('0')

f = open('B-small-attempt0.in', 'r')
o = open('output', 'w')
t = f.readline()
strf = "Case #{case}: {tn}"

c = 0
for n in f:
    c += 1
    tidy_n = tidy(n.strip())
    print('old: ', n.strip(), ' new: ', tidy_n)
    o.write(strf.format(case = c, tn = tidy_n))
    if( c < int(t)):
        o.write("\n")


