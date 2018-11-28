
fin = open('B-large.in')
fout = open('magicka.out', 'w')


cases = int(fin.readline())

for case_index in range(cases):
    bits = iter(fin.readline().strip().split())
    comb_num = int(bits.next())
    combining = {}
    opposed = []
    for i in range(comb_num):
        three = bits.next()
        combining[tuple(sorted([three[0], three[1]]))] = three[2]
    
    opp_num = int(bits.next())
    for i in range(opp_num):
        two = bits.next()
        opposed.append(tuple(sorted([two[0], two[1]])))
    
    chars = int(bits.next())
    to_invoke = bits.next()[:chars]
    
    elems = []
    
    for e in to_invoke:
        if not elems:
            elems.append(e)
        else:
            key = tuple(sorted([e, elems[-1]]))
            if combining.has_key(key):
                elems.pop()
                elems.append(combining[key])
            else:
                cleared = False
                for e1 in elems:
                    key = tuple(sorted([e, e1]))
                    if key in opposed:
                        elems = []
                        cleared = True
                        break
                if not cleared:
                    elems.append(e)
    fout.write('Case #%d: [%s]\n' % (case_index + 1, ', '.join(elems)))

fin.close()
fout.close()


