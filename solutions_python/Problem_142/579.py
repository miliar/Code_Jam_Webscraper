# Google Code Jam 2014 Round 1B
# Problem A
# Shaotong Wang

def one_empty(strs):
    for i in xrange(len(strs)):
        if len(strs[i]) == 0:
            return True
    return False

def all_empty(strs):
    for i in xrange(len(strs)):
        if len(strs[i]) != 0:
            return False
    return True

def fst_diff(strs):
    fst = strs[0][0]
    for i in xrange(1,len(strs)):
        if strs[i][0] != fst:
            return True
    return False

def first_len(stri):
    fst = stri[0]
    res = 1
    for i in xrange(1,len(stri)):
        if fst == stri[i]:
            res = res+1
        else:
            return res
    return res

fin = open('A.in', 'r')
fout = open('A.out', 'w')

num_cases = int(fin.readline())

for case in range(1,num_cases+1):
    
    strs = range(0, int(fin.readline()))
    for i in xrange(len(strs)):
        strs[i] = fin.readline()[:-1]

    num_moves = 0
        
    while True:
        if all_empty(strs):
            break
        if one_empty(strs) or fst_diff(strs):
            num_moves = -1
            break
        else:
            first_lens = map(first_len, strs)
            #print strs, first_lens
            avg = int(round(float(sum(first_lens))/float(len(first_lens))))
            for i in xrange(len(first_lens)):
                num_moves = num_moves + abs(avg-first_lens[i])
            for i in xrange(len(strs)):
                strs[i] = strs[i][first_lens[i]:]

    fout.write("Case #" + str(case) + ": ")
    if num_moves == -1:
        fout.write("Fegla Won")
    else:
        fout.write(str(num_moves))
    fout.write("\n")
        

fin.close()
fout.close()

