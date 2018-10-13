'''input
4
132
1000
7
111111111111111110
'''
def is_tidy(n, i):
    if i == len(n) - 1:
        return True
    return n[i] <= n[i + 1] and is_tidy(n, i+1)

T = int(input())
for t in range(T):
    N = list(map(int, input()))
    while not is_tidy(N, 0):
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
                N[i] -= 1
                for j in range(i + 1, len(N)):
                    N[j] = 9 

    print("Case #{}: {}".format(t+1,''.join(map(str, N)).strip('0')))