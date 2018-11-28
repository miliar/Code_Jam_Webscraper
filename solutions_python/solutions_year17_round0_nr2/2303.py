import heapq
def print_answer(casenum, ans):
    print('Case #{0}: {1}'.format(casenum, ans))

def solve(N, K):
    pass

def is_tidy(n):
    n = str(n)
    return all(n[i]<= n[i+1] for i in range(len(n)-1))

def simulation(N):
    for i in range(N, 1, -1):
        if is_tidy(i):
            return i
    return 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        ans = simulation(N)
        print_answer(i+1, ans)

def test():
    pass
if __name__ == '__main__':
    main()
    # test()