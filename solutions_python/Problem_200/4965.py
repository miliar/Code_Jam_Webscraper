
def checkTidy(i):
    a = str(i)
    prev = a[0]
    for ch in a[1:]:
        if int(prev) > int(ch):
            return False
        prev = ch
    return True


def Solve(N):
    if len(N) <= 1:
        return N
    N = int(N)
    for i in xrange(N,0,-1):
        if len(str(i)) > 1:

            Tidy = checkTidy(i)

            if Tidy == True :
                return i
        else :
            return i


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1,T+1):
        N = f.readline()
        num = Solve(N.rstrip('\n'))
        print ("Case #"+str(case)+": "+str(num))