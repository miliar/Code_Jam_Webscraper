def answer(num):

    if int(num) < 10:
        return int(num)

    digs = [int(s) for s in str(num)]

    resultStr = num

    while sorted(digs) != digs:

        idx = len(digs) - 1

        for i in range(len(digs)-1,0,-1):
            if digs[i] < digs[i-1]:
                idx = i - 1
                break


        digs = digs[:idx] + [digs[idx]-1] + [9 for i in digs[idx+1:]]

        resultStr = ''
        for d in digs:
            resultStr += str(d)

    return int(resultStr)


import sys

def main():

    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in range(nums):
            n, = f.readline().strip().split()
            n = int(n)

            r = answer(n)
            print("Case #{:d}: ".format(i+1)+str(int(r)))


main()
