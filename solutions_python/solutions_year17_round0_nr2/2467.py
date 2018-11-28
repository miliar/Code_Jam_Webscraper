from sys import stdin

T = int(stdin.readline())
for t in range(1, T+1):
    number = [int(a) for a in stdin.readline().strip()]
    N = len(number)
    while number != sorted(number):
        for i in range(N-2, -1, -1):
            if number[i] > number[i+1]:
                number[i] -= 1
                for j in range(i+1, N):
                    number[j] = 9
                break
    while number[0] == 0:
        number = number[1:]
    print "Case #%d: %s" % (t, "".join([str(a) for a in number]))
