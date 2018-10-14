f = open("in.txt", "r")
out = open("out.txt", "w")
cases = int(f.readline())
case = 0

for line in f:
    sol = 0
    x = line.split()
    A = int(x[0])
    B = int(x[1])

    for m in range (A,B+1):
        num = str(m)

        for i in range(1,len(num)):
            test_str = num[-1]+num[:-1]
            test = int(test_str)

            if (test>m and test<=B):
                sol = sol+1
                if (len(num) % 2 == 0) and (num[:len(num)/2] == num[len(num)/2:]):
                    break

            num = test_str


            
    case=case+1
    out.write("Case #"+str(case)+": "+str(sol)+"\n")
