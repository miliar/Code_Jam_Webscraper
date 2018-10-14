from collections import deque
import time


def main():
    path = "C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\B.Tidy\\"
    with open(path + "result" + str(time.time()) + ".txt", 'w') as resF:
        T, nums = readFile(path + "\\B-large.in")
        for i in xrange(T):
            res = solve(nums[i])
            resF.write("Case #" + str(i+1) + ": " + str(res) + "\n")


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) == 0:
            print "Err reading"
        T = int(lines[0].replace("\n", ""))

        nums = []
        for i in xrange(1, T+1):
            nums.append(int(lines[i].replace("\n", "")))

        return (T, nums)

def solve(num):
    digs = [int(ch) for ch in str(num)]
    #print str(num) + " , "  + str(digs)

    last_nine = len(digs)
    for i in xrange(len(digs)-1, 0, -1):
        if digs[i] < digs[i-1]:
            digs[i-1] -= 1
            digs[i:last_nine] = [9]*(last_nine-i)
            #print str(digs).replace(", ", "")[1:-1]
            last_nine = i

    return int(str(digs).replace(", ", "")[1:-1])

if __name__ == '__main__':
    main()

