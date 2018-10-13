import sys

def main():
    infile, outfile = sys.argv[1:3]
    with open(infile, 'r') as inp:
      with open(outfile, 'w') as out:
        T = int(inp.readline())
        for case in range(1, T+1):
            N = int(inp.readline())
            S = []
            for i in range(N):
                S.append(inp.readline()[:-1])
            ans = find_solution(N, S)
            if ans == -1:
                ans = 'Fegla Won'
            out.write('Case #{}: '.format(case))
            out.write('{}\n'.format(ans))

def find_solution(N, S):
    K = []
    for i in range(N):
        if not S[i]:
            return -1
        last_char = S[i][0]
        p = last_char
        n = 1
        num_lst = []
        for j in range (1, len(S[i])):
            c = S[i][j]
            if c == last_char:
                n +=1
            else:
                p += c
                num_lst.append(n)
                last_char = c
                n = 1
        num_lst.append(n)
        K.append((p, num_lst))
    for i in range(1, len(K)):
        if K[i][0] != K[i-1][0]:
            return -1
    l = len(K[i][0])
    opt = [0]*l
    for (s, lst) in K:
        for j in range(len(lst)):
            opt[j] += lst[j]
    for j in range(len(opt)):
        opt[j] //= len(K)
    ans = 0
    for (s, lst) in K:
        for j in range(len(lst)):
            ans += abs(lst[j]-opt[j])
    return ans

if __name__ == '__main__':
    main()
