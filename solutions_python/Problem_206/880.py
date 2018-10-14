from sys import stdin, stdout


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def solve_case():
    D, N = read_ints()
    K, S = [0] * N, [0] * N
    for i in range(N):
        K[i], S[i] = read_ints()
        
    max_t = 0
    for i in range(N - 1, -1, -1):
        max_t = max(max_t, (D - K[i]) / S[i])
    
    return D / max_t

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {:.6f}'.format(case, solve_case()))
        stdout.flush()

        
if __name__ == '__main__':
    main()
