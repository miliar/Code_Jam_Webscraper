def main():
    T = int(input())
    for i in range(T):
        Ns = input()
        l = len(Ns)
        N = int(Ns)
        Nans = [9 for i in range(l-1)]
        Ntmp = [ord(Ns[0])-ord('0')] + [9 for i in range(l-1)]
        carry = 0
        for j in range(1, l):
            digit = (ord(Ns[j])-ord('0'))
            current = carry + ((ord(Ns[j-1])-ord('0'))*10+ord(Ns[j])-ord('0'))

            if digit < Ntmp[j-1]:
                if Ntmp[j-1]*10+digit >= current:
                    for k in range(j-1, -1, -1):
                        if k == 0:
                            break
                        elif Ntmp[k]-1 >= Ntmp[k-1]:
                            break
                        else:
                            Ntmp[k] = 9
                    Ntmp[k] -= 1
                    carry += 10**(l-k-1)
                Ntmp[j] = 9

            else:
                Ntmp[j] = digit

        print('Case #{}: {}'.format(i+1, int(''.join([str(n) for n in Ntmp]))))

if __name__ == '__main__':
    main()
