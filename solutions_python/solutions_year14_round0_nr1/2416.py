def solve(r1, a1, r2, a2):
    s = set(a1[r1 - 1].split(' ')).intersection(a2[r2 - 1].split(' '))
    l = len(s)
    
    if l == 0:
        return 'Volunteer cheated!'
    elif l == 1:
        return s.pop()
    else:
        return "Bad magician!"

def read_input():
    r1 = int(raw_input())
    a1 = []
    for i in range(4):
        a1.append(raw_input())
    r2 = int(raw_input())
    a2 = []
    for i in range(4):
        a2.append(raw_input())
    return r1, a1, r2, a2

for case_n in range(1, int(raw_input()) + 1):
	print 'Case #%s: %s' % (case_n, solve(*read_input()))
