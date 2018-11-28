case_prefix = 'Case #'


def num_recycled(a, b):
    if a >= b:
        return 0
    num = 0

    L = len(str(a))
    if L == 1:
        return 0

    pairs = dict()
    for i in range(a, b + 1):
        A = str(i)
        for j in range(L):
            B = A[L - 1 - j :] + A[0 : L - 1 - j]
            possible_b = int(B)
            if possible_b > i and possible_b <= b and possible_b not in pairs.get(i, set()) and i not in pairs.get(possible_b, set()):
                num += 1
                s = pairs.get(i, set())
                s.add(possible_b)
                pairs[i] = s
                s = pairs.get(possible_b, set())
                s.add(i)
                pairs[possible_b] = s
    
    return num
            
        

f = open('C-small-attempt0.in', 'r')
num_tests = int(f.readline().strip())
for case in range(num_tests):
    words = f.readline().strip().split()
    a, b = int(words[0]), int(words[1])

    print case_prefix + str(case + 1) + ': ' + str(num_recycled(a, b))
f.close()
