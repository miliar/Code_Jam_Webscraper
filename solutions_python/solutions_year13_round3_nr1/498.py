__author__ = 'eiPi10'

of = open('A-small-attempt0.out', 'w')

f = open('A-small-attempt0.in', 'r')

counter = 0
number_of_test_cases = 0
cases = []
name, n = '', 0
vowels = ['a', 'e', 'i', 'o','u']

for line in f:
    if counter==0:
        number_of_test_cases = int(line)
    else:
        name, n = line.split()
        cases.append((name, int(n)))
    counter += 1

if len(cases)<number_of_test_cases:
    cases.append((name, int(n)))

if(len(cases)!=number_of_test_cases):
    raise ValueError('number of test cases read from file does not match the indicated number of test cases that should be there')

f.close()

for i, case in enumerate(cases):
    name, n = case
    cont = True
    cont_cons_range_set = set()

    for j in range(len(name)-n+1):
        substr = name[j:j+n]
        for v in vowels:
            if v in substr:
                cont = False
                break
        if cont:
            rang = [j,j+n]
            cont_cons_range_set.add(tuple(rang))
            tmp = [tuple(rang)]

            for k in range(j+1):
                s = rang[0]-k
                e = rang[1]
                cont_cons_range_set.add((s,e))
                tmp.append((s,e))

            for l in range(j+n, len(name)+1):
                for t in tmp:
                    cont_cons_range_set.add((t[0], l))


        cont = True

    #print name, len(cont_cons_range_set), cont_cons_range_set

    #print 'Case #%d: %d'%(i+1, len(cont_cons_range_set))
    of.write('Case #%d: %d'%(i+1, len(cont_cons_range_set)))

    of.write('\n')
of.close()

 

 