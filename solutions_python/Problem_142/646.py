T = int(raw_input())

template = "Case #{}: {}"

def decompose(string):
    res = []
    for k, c in enumerate(string):
        if k > 0 and c == string[k-1]:
            res[-1][1] += 1
        else:
            res.append([c, 1])
    return res

for i in xrange(1, T+1):
    N = int(raw_input())

    a = []
    for j in xrange(N):
        a.append(decompose(raw_input()))

    f_won = False
    for j in xrange(len(a[0])):
        for pairs in a:
            if len(pairs) != len((a[0])) or pairs[j][0] != a[0][j][0]:
                f_won = True
    if f_won:
        print template.format(i, "Fegla Won")
        continue
    only_numbers = [ [pair[1] for pair in pairs ] for pairs in a]
    #print only_numbers
    sums = [ sum([k[j] for k in only_numbers]) for j in xrange(len(only_numbers[0])) ]
    #print sums
    avgs = [ int(round(x/float(N), 0)) for x in sums]
    #print avgs
    movies = sum([ sum([abs(x - y) for x,y in zip(num_seq, avgs)]) for num_seq in only_numbers])
    print template.format(i, movies)
