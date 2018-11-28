def perms(number_str, number_str_len):
    for i in range(1, number_str_len):
        begin = number_str[:number_str_len-i]
        end = number_str[number_str_len-i:]
        compound = end + begin
        yield compound

pairs = []

def permutations(A, B, number):
    score = 0
    number_str = str(number)
    for perm in perms(number_str, len(number_str)):
        nb = int("".join(perm))
        if nb != number and nb >= A and nb <= B and (min(number, nb),
                max(number, nb)) not in pairs:
            score += 1
            pairs.append((min(number, nb), max(number, nb))) 
    return score

def problem(i, A, B):
    pairs = []
    score = 0

    for number in range(A, B+1):
        score += permutations(A, B, number) 

    return "Case #%d: %d" % (i+1, score)

if __name__ == '__main__':
    import sys

    T = int(sys.stdin.readline())

    for i in xrange(T):
        pairs = []
        A, B = map(int, sys.stdin.readline().strip().split(" "))
        print problem(i, A, B)

