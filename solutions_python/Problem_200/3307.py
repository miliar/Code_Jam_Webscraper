T = int(input())
for case in range(T):
    N = input()
    R = "0"
    for digit in range(len(N),0,-1):
        for n in range(9,int(R[-1])-1,-1):
            R = R[0:len(N)-digit] + digit*str(n)
            if(int(R) <= int(N)):
                break;
    R = R.strip('0')       
    print("Case #{}: {}".format(case+1, R))


