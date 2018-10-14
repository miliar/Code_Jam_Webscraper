
def flip(pancakes, i, k):
    for j in range(k):
        if pancakes[i + j] == '+':
            pancakes[i+j] = '-'
        else:
            pancakes[i+j] = '+'
    return pancakes

def solve():
    pancakes, k = raw_input().split()
    k = int(k)
    pancakes = list(pancakes)
    sol = 0
    for i in range(0, len(pancakes)-k+1):
        if pancakes[i] == '+':
            continue
        pancakes = flip(pancakes, i, k)
        sol += 1
    if set(pancakes) == set(['+']):
        return sol
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        print "Case #{}: {}".format(i, solve())
