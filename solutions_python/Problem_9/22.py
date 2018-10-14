import sys, os
##
file_in = 'C-small-attempt0.in'
file_out = 'C-small.out'
##file_in = 'C-large.in'
##file_out = 'C-large.out'
##file_in = 'test.txt'
##file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')

def compute_deck(n, indices):
    deck = []
    starting_value = {}
    for i in range(n):
        deck.append(i)
    for i in range(n):
        index = i % len(deck)
        start = deck[index]
        starting_value[start+1] = i+1
        deck = deck[index+1:]+deck[:index]

    result = []
    for k in indices:
        result.append(str(starting_value[k]))

    return ' '.join(result)

test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    l = f.readline().strip('\n')
    K = int(l)
    l = f.readline().strip('\n')
    l = l.split()
    n = int(l[0])
    indices = [int(x) for x in l[1:]]

    res = compute_deck(K, indices)

    print >> res_f, "Case #%s: %s" % ((i+1), res)


try:
    f.close()
    res_f.close()
except:
    pass

print "done"