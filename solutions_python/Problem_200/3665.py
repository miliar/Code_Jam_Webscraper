def solve(n):
    stack = []
    while n > 0:
        stack.append(n % 10)
        n /= 10
    ret = cur = stack.pop()
    # keep track of equal sequence
    equal_seq = 0
    while len(stack) > 0:
        nxt = stack.pop()
        if nxt < cur:
            if equal_seq == 0:
                return ret * (10 ** (len(stack) + 1)) - 1
            else:
                return (ret / (10 ** equal_seq)) * (10 ** equal_seq) * (10 ** (len(stack) + 1)) - 1
        elif nxt == cur:
            equal_seq += 1
        else:
            equal_seq = 0
        cur = nxt
        ret = ret * 10 + cur
    return ret

if __name__ == "__main__":
    # print solve(132)
    # print solve(1000)
    # print solve(7)
    # print solve(111111111111111110)

    # inputs = open('./B-small-attempt0.in.txt')
    inputs = open('./B-large.in.txt')
    outputs = open('./outputs.txt', 'w')
    T = int(inputs.readline())
    for c in range(1, T + 1):
        N = int(inputs.readline())
        sol = solve(N)
        outputs.write("Case #{0}: {1}\n".format(c, sol))
    inputs.close()
    outputs.close()
