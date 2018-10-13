def solve(N, K):
    state = bin(K)[2:][-N:]
    return 'ON' if state == N * '1' else 'OFF'
    
def main():
    file = open('A-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        N, K = [int(x) for x in file.readline().split()]
        print >> output, 'Case #%d:' % case, solve(N, K)
    output.close()
    
if __name__ == '__main__':
    main()
    
