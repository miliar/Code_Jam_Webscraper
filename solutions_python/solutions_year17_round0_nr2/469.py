def solve(n):
    first_decreaser = -1
    start_of_block = 0
    current_digit = int(n[0])
    for i in xrange(1, len(n)):
        ni = int(n[i])
        if ni > current_digit:
            current_digit = ni
            start_of_block = i
        elif ni < current_digit:
            first_decreaser = i
            break

    if first_decreaser == -1:
        return n

    answer = ""
    
    if current_digit == 1:
        for i in xrange(0, len(n) - 1):
            answer = answer + '9'
        return answer

    nines = len(n)
    for i in xrange(0, start_of_block):
        answer = answer + n[i]
        nines = nines - 1

    answer = answer + str(current_digit - 1)
    nines = nines - 1

    for i in xrange(0, nines):
        answer = answer + '9'
    
    return answer

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    print "Case #{}: {}".format(i, solve(n))
