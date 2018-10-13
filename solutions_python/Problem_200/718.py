
def main():
    with open('B-small-attempt0.in') as f:
        t = int(f.readline())
        for i in range(t):
            n = f.readline()
            n = n[:-1]
            n = list(n)
            idx = len(n)
            for j in range(len(n)-1,0,-1):
                if (n[j-1] > n[j]):
                    idx = j
                    n[j-1] = str(int(n[j-1])-1)
            for j in range(idx, len(n)):
                n[j] = '9'
            print('Case #{}: {}'.format(i+1, int(''.join(n))))

if __name__ == "__main__":
    main()
