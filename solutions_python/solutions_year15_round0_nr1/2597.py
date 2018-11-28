def solve(n, l):
    if n == 0:
        return 0
    
    current = 0
    required = 0

    for i in range(0,n+1):
        if current < i:
            a = i-current
            required += a
            current += a
        current += l[i]
    return required
    

input_text = [line.strip() for line in open('q1b.txt')]

CASE_COUNT = int(input_text[0])

for CASE_NUM in range(1,CASE_COUNT+1):
    p = input_text[CASE_NUM].split(' ')
    n = int(p[0])
    l = [int(x) for x in p[1]]
    print "Case #%d: %d" % (CASE_NUM, solve(n,l))