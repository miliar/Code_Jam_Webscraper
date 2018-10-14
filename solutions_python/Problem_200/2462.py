file = open("input.in", 'r').readlines()

t = int(file[0])

with open("output.out", 'w') as f:
        for r in range(t):
            n = int(file[r+1])

            found = False
            while not found:
                last = 9
                s = str(n)[::-1]
                for i in range(len(s)):
                    d = int(s[i])
                    if d > last:
                        s = '9'*i + str(d-1) + s[i+1:]
                        break
                    last = d
                else:
                    found = True
                n = int(s[::-1])
                print(n)

            print(n)
            f.write("Case #"+str(r+1)+": "+str(n)+'\n')
