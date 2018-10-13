from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def solve_case():
    N = read_str()
    
    len_N = len(N)
    
    if len_N == 1:
        return N

    N = list(map(int, list(N)))
        
    i = len_N - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            if N[j] > N[i]:
                N[j] -= 1
                for k in range(j + 1, len_N):
                    N[k] = 9
                i = j + 1
                break
            j -= 1
        i -= 1
        
    if N[0] == 0:
        N = N[1:]
    
    return ''.join(map(str, N))

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
if __name__ == '__main__':
    main()
