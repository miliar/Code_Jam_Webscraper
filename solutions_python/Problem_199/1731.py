from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def solve_case():
    pancakes, K = read_strs()
    pancakes = list(pancakes)
    K = int(K)
        
    flips = 0
    
    i = 0
    len_pancakes = len(pancakes)
    while i < len_pancakes - K:
        if pancakes[i] == '-':
            flips += 1
            j = i
            while j < i + K:
                pancakes[j] = '+' if pancakes[j] == '-' else '-'    
                j += 1
        i += 1
    
    s = pancakes[i]
    if s == '-':
        flips += 1
    
    i += 1
    while i < len_pancakes:
        if pancakes[i] != s:
            return 'IMPOSSIBLE'
        i += 1
    
    return flips

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
if __name__ == '__main__':
    main()
