def find_equal_sums(lst):
    values_seen = dict()
    for i in xrange(1, 2**len(lst)):
        i = bin(i)[2:].zfill(len(lst))
        s = sum(lst[x] for x in range(len(lst)) if int(i[x]))
        if values_seen.has_key(s):
            old_indices = values_seen[s]
            new_indices = i
            
            oldlst = []
            newlst = []
            for j in range(len(lst)):
                if old_indices[j] == '1' and new_indices[j] != '1':
                    oldlst.append(lst[j])
                if new_indices[j] == '1' and old_indices[j] != '1':
                    newlst.append(lst[j])
            
            return (oldlst, newlst)
        else:
            values_seen[s] = i
    return None

outputlist = []

for i, testcase in enumerate(open('C-small-attempt0.in', 'r').read().splitlines()[1:]):
#for i, testcase in enumerate(open('EqSuTst.txt', 'r').read().splitlines()[1:]):
    nums = testcase.split()[1:]
    nums = map(int, nums)
    x = find_equal_sums(nums)
    outputlist.append('Case #%i:' % (i+1))
    if x is None:
        outputlist.append('Impossible')
    else:
        outputlist.append(' '.join(map(str, x[0])))
        outputlist.append(' '.join(map(str, x[1])))

outputfile = open('EqualSumsOutputSmall.txt', 'w')
outputfile.write( '\n'.join(outputlist) )