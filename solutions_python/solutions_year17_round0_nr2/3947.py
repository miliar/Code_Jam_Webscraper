def tidy(n):
    flag = True
    last = 10

    while (n > 0) and (flag):
        now = n % 10
        if now > last:
            flag = False
        last = now
        n = n//10

    return flag

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        while not tidy(N):
            N = N-1
        print('case #%d: %d' % (t+1, N))

if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            break
