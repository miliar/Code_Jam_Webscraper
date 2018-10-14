def diff(score, p):
    if (p == 0):
        return 0
    if (p >= score):
        return 100
    if (score / 3 >= p):
        return 0
    else:
        a = (score - p) / 2
        return p - a

def diff1(score,p):
    if (p == 0):
        return 0
    if (p > score):
        return 100
    if (score < p * 3 - 4):
        return 100
    if (score >= p * 3 - 4 and score < p * 3 - 2):
        return 2
    if (score >= p * 3 -2 and score < p * 3):
        return 1
    return 0
  

def num_p(line):
    inp = line.split()
    N = int(inp[0])
    S = int(inp[1])
    p = int(inp[2])
    count = 0
    count_odd = 0
    for i in range(3,len(inp)):
        d = diff(int(inp[i]), p)
        if (d < 2):
            count += 1
        if (d == 2):
            count_odd += 1
    

    if (count_odd > S):
        count_odd = S
    count += count_odd
    return count

def num_p1(line):
    inp = line.split()
    N = int(inp[0])
    S = int(inp[1])
    p = int(inp[2])
    count = 0
    count_odd = 0
    for i in range(3,len(inp)):
        d = diff1(int(inp[i]), p)
        if (d < 2):
            count += 1
        if (d == 2):
            count_odd += 1
    

    if (count_odd > S):
        count_odd = S
##    if (count_odd != S):
##        print "!!!", line
    count += count_odd
    return count

f = open('C:\\B-large.in')
f_out = open('C:\\res.txt','r+')
j = 0
n = 0
for line in f:
    if (j == 0):
        n = int(line)
        j = j + 1
        continue
    f_out.write("Case #"+str(j)+": "+str(num_p1(line))+'\n')
    #print line, num_p(line), num_p1(line)
    j = j + 1


f.close()
f_out.close()

