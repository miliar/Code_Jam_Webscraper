import sys
def rotated_numbers(n):
    n_str = str(n)
    result = set()
    for i in range(len(n_str)):
        candidate = n_str[i:] + n_str[:i]
        if candidate[0] != '0':
            result.add(int(candidate))
    return result        
n_cases = int(sys.stdin.readline())
for case_n in range(1, n_cases+1):
    (a_str, b_str) = sys.stdin.readline().strip().split()
    a = int(a_str)
    b = int (b_str)
    answer = 0
    for n in range(a, b):
        ms = rotated_numbers(n)
        for m in ms:
            if n < m <= b:
                answer += 1
    print "Case #%d: %d" % (case_n, answer)
