def empty_seq(seq):
    beginning = 0
    length = 0
    current_length = 0
    current_beginning = 0
    for i in xrange(len(seq)):
        if seq[i] == 1:
            if current_length > length:
                length = current_length
                beginning = current_beginning
            current_length = 0
        else:
            if current_length == 0:
                current_beginning = i
            current_length += 1
    return beginning, length + beginning - 1

def find_stall(seq):
    b, e = empty_seq(seq)
    return (b + e) // 2

def left(pos, seq):
    dist = 0
    pos -= 1
    while seq[pos] == 0:
        pos -= 1
        dist += 1
    return dist

def right(pos, seq):
    dist = 0
    pos += 1
    while seq[pos] == 0:
        pos += 1
        dist += 1
    return dist

T = int(raw_input())
test_cases = []
for case in xrange(T):
    test_cases.append(raw_input())

for case in xrange(len(test_cases)):
    N, K = test_cases[case].split()
    N, K = int(N), int(K)
    stalls = [1] + [0] * N + [1]
    for user in xrange(K):
        s = find_stall(stalls)
        stalls[s] = 1
    answer = "Case #" + str(case + 1) + ": "
    answer += str(max(left(s, stalls), right(s, stalls))) + " "
    answer += str(min(left(s, stalls), right(s, stalls)))
    print answer
    