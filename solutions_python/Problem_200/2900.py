for j in range(int(input())):
    N = int(input())

    def tidy():
        global N
        if N < 10:
            return True
        i_0 = str(N)[0]
        for i in range(1, len(str(N))):
            if int(i_0) <= int(str(N)[i]):
                i_0 = str(N)[i]
            else:
                N1 = N // (10**(len(str(N)) - i)) * (10**(len(str(N)) - i))
                if N1 == N:
                    N -= 1
                else:
                    N = N1
                return False
        return True

    while not tidy():
        pass
    print('Case #' + str(j + 1) + ': ' + str(N))
