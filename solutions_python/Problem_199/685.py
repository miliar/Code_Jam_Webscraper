
def main():
    with open('A-small-attempt0.in') as f:
        n = int(f.readline())
        for i in range(n):
            s, k = f.readline().split()
            s = list(s)
            k = int(k)
            flips = 0
            #print('k:{}'.format(k))
            #print(''.join(s))
            for j in range(len(s)-k +1):
                if s[j] == '-':
                    flips += 1
                    if(len(s) -j < k):
                        break
                    for l in range(j, j+k):
                        if l == len(s):
                            break
                        s[l] = '-' if s[l] == '+' else '+'
                #print(''.join(s))
            if '-' in s:
                print('Case #{}: IMPOSSIBLE'.format(i+1))
            else:
                print('Case #{}: {}'.format(i+1, flips))

if __name__ == "__main__":
    main()
