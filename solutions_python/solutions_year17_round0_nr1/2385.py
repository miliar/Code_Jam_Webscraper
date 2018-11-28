import sys
def turn(s, k):
    turns = 0 
    for j in range(0,len(s)-k+1):
        if s[j] == '-':
            turns += 1
            for i in range(j,j+k):
                if s[i] == '-':
                    s[i] = '+'
                elif s[i] == '+':
                    s[i] = '-'
    k_positive = "+"*len(s)
    if ''.join(s) == k_positive:
        return turns
    else:
        return "IMPOSSIBLE"
f = 101
for p in range(1, int(f)):
    case = raw_input()
    b = str(case).split()
    turns = turn(list(b[0]), int(b[1]))
    print "Case "+"#"+ str(p) + ": " + str(turns)