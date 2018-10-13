
def main():
    with open('C-small-attempt0.in') as f:
        t = int(f.readline())
        for j in range(t):
            n, k = f.readline().split()
            n = int(n)
            k = int(k)
            v = (n, 1, n+1, 0)
            o = 0
            i = 1
            while (o + i < k):
                o += i
                if v[0] % 2 == 0:
                    v = (v[0]/2-1, v[1], v[0]/2, v[3]*2 + v[1])
                else:
                    v = (v[0]/2, v[1]*2+v[3], v[0]/2+1, v[3])
                i *= 2
                #print('v: {}, i: {}, o: {}'.format(v, i, o))
            if v[3] >= k-o:
                sol = v[2]
            else:
                sol = v[0]
            print('Case #{}: {} {}'.format(j+1, sol/2, (sol-1)/2))

if __name__ == "__main__":
    main()
