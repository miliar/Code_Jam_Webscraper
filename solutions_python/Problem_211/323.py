# Andrew Savage
# code jam 1c p3

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        inp = raw_input().split(" ")
        N = int(inp[0])
        K = int(inp[1])
        units = float(raw_input())
        str_probs = raw_input().split(" ")
        probs = []
        for p in str_probs:
            probs.append(float(p))

        #print N, K, units, probs
        probs = solve(N, K, units, probs)
        get_f_prob(N, K, probs, i)

def solve(N, K, units, probs):
    probs = sorted(probs)
    probs = probs[(N - K):]
    #print probs

    num_same = 0
    same_amt = probs[0]
    for i in range(len(probs)):
        if same_amt == probs[i]:
            num_same += 1
    #print num_same

    while units > 0:
        if num_same == len(probs):
            add = units / len(probs)
            for i in range(len(probs)):
                probs[i] += add
            break

        add = 0
        diff = probs[num_same] - probs[num_same - 1]
        if units < diff * num_same:
            add += units / num_same
        else:
            add += diff

        for i in range(num_same):
            probs[i] += add
        units -= add * num_same
        num_same += 1

    #print probs
    return probs

def get_f_prob(N, K, probs, case):
    if N == K:
        prob = 1.0
        for i in range(len(probs)):
            prob *= probs[i]
        print "Case #{0}: {1}".format(case, prob)
        return
        
    prob = 0.0
    for i in range(K, N + 1):
        prob += gh(N, i, probs)
    print "Case #{0}: {1}".format(case, prob)

def gh(N, K, probs):
    if K == 1:
        prob = 1.0
        for i in range(len(probs)):
            prob *= (1.0 - probs[i])
        return (1.0 - prob)

    prob = 0.0
    for i in range(len(probs)):
        prob += probs[i] * gh(N - 1, K - 1, (probs[0:i] + probs[i + 1: len(probs)]))
    return prob
    
    
main()
