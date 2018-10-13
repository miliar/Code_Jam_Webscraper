def answer(n):
    n = [int(d) for d in str(n)]
    lenn = len(n)
    if (lenn == 1):
        return n[0]
    else:
        for i in range(lenn-1, 0, -1):
            last = n[i]
            second_last = n[i-1]
            if(last < second_last):
                n[i] = 9
                n[i-1] = int(n[i-1]) - 1
                for j in range(i, lenn-1):
                    if(n[j] > n[j+1]):
                        n[j+1] = n[j]
        return (int(''.join(map(str, n))))

testCase = int(input())
for etc in range(testCase):
    print ("Case #" + str(etc + 1) + ": " + str(answer(int(input()))))
