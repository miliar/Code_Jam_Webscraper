import itertools

def solve(N, K, B, T, X, V):
    swaps, can_reach, prev = 0, 0, 0
    for x, v in reversed(zip(X, V)):
        if T * v >= B - x:
            swaps += prev - can_reach
            can_reach += 1
        if can_reach == K:
            break
        prev += 1
    else:
        return 'IMPOSSIBLE'
    return swaps
    
def main():
    file = open('B-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        N, K, B, T = [int(x) for x in file.readline().split()]
        X = [int(x) for x in file.readline().split()]
        V = [int(x) for x in file.readline().split()]
        print >> output, 'Case #%d:' % case, solve(N, K, B, T, X, V)
    output.close()

if __name__ == '__main__':
    main()

    
