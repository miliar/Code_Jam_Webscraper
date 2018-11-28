# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def check_all_happy(pancakes):
    for p in pancakes:
        if p != '+': return False
    return True

def flip(p):
    if p == '-': return '+'
    else: return '-'

def solution(pancakes, k):
    count = 0
    if check_all_happy(pancakes): return count
    for index, p in enumerate(pancakes):
        if p == '-':
            count += 1
            for j in range(k):
                if index + j > len(pancakes) - 1:
                    answer = 'IMPOSSIBLE'
                    return answer
                pancakes[index + j] = flip(pancakes[index + j])
    return count

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    pancakes_string, k = [s for s in raw_input().split(" ")]
    pancakes = [p for p in pancakes_string]
    answer = solution(pancakes, int(k))

    print "Case #{}: {}".format(i, answer)
