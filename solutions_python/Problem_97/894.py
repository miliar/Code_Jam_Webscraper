__author__ = 'diana_fisher'

# given integers A and B with the same number of digits,
# how many distinct recycled pairs (n,m) are there with A <= n < m <= B?

def count_recycled_pairs(A, B):
    pairs = []
    max_sub_length = len(A) - 1
#    print 'max_sub_length=', max_sub_length
    A_val = int(A)
    B_val = int(B)
    for n in range(A_val, B_val):
        n_str = str(n)
#        print 'n=',n
        length = 1
        while length <= max_sub_length:
            s = n_str[:length]
            s2 = n_str[length:]
#            print 's:', s, 's2:',s2
            m_str = s2 + s
#            print 'm:', m
            m = int(m_str)
            if m > n and m <= B_val:
#                print 'm greater than n', m, '>', n
                pair = m_str+n_str
#                print 'pair', pair
                if pair not in pairs:
                    pairs.append(pair)
            length += 1

    return len(pairs)

filename = "C-small-attempt0.in"
file = open(filename, "r")
lines = []
for line in file:
    lines.append( line.strip() )

file.close()

numCases = int(lines[0])
for i in range(1, numCases+1):
#    print '----------------------------------------------------'
    case = "Case #" + str(i) + ":"
    line = lines[i]
    items = line.split()
#    print items
    A = items[0]
    B = items[1]
    num = count_recycled_pairs(A,B)
    print case, num