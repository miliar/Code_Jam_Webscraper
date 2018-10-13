import sys, re, math

def palindrome(num):
    string = str(num)
    for i in range(len(string) / 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

if __name__ == "__main__":
    line = raw_input()
    T = int(line.rstrip())
    for t in range(T):
        count = 0
        line = raw_input()
        vector = line.rstrip().split()
        mini, maxi = (int(item) for item in vector)
        for num in range(mini, maxi + 1):
            sq = int(math.sqrt(num))
            if math.pow(sq, 2) == num and palindrome(sq) and palindrome(num):
                count += 1
        print "Case #%d: %d" % (t + 1, count)
