__author__ = 'sushrutrathi'

IM = "IMPOSSIBLE"

clo = open("output.txt", 'w')

with open("input.txt") as f:
    t = int(f.readline())
    for test in range(1,t+1):
        arr = f.readline().strip().split(' ')
        st = arr[0]
        k = int(arr[1])
        n = len(st)
        if n < k:
            clo.write("Case #" + str(test) + ": " + IM)
        else:
            ans = 0
            for i in range(0,n-k+1):
                if st[i] == '-':
                    ans += 1
                    for j in range(k):
                        if st[i+j]== '-':
                            st = st[0:i+j] + '+' + st[i+j+1:]
                            #st[i+j] = '+'
                        else:
                            st = st[0:i+j] + '-' + st[i+j+1:]

            mm = False
            for i in range(n):
                if st[i]=='-':
                    mm = True
                    break

            if mm:
                clo.write("Case #" + str(test) + ": " + IM)
            else:
                clo.write("Case #" + str(test) + ": " + str(ans))


        clo.write("\n")

