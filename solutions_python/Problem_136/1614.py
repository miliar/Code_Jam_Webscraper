__author__ = 'Lucas'


def testCase(C, F, X, w, num):
    rate = 2
    time = 0
    cookies = 0
    if X < C:
        cookies = X
        time += X/rate
    while cookies < X:
        if cookies < C:
            cookies = C
            time += C/rate
        else:
            nowTimeToFinish = (X - cookies)/rate
            potentialNewRate = rate + F
            potentialTimeToFinish = X/potentialNewRate
            if potentialTimeToFinish < nowTimeToFinish:
                cookies = 0
                rate += F
            else:
                cookies = X
                time += nowTimeToFinish
    w.write("Case #" + str(num) + ": " + str(time))
    w.write("\n")


def main():
    f = open('input.in', 'r')
    w = open('output.out', 'w')

    T = int(f.readline().split()[0])
    for t in range(T):
        line = list(map(float, f.readline().split()))
        C = line[0]
        F = line[1]
        X = line[2]
        testCase(C, F, X, w, t+1)



if __name__ == "__main__": main()