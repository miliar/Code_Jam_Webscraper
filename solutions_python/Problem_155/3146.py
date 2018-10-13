def main():
    data = open("data")
    testCases = int(data.readline())
    for t in xrange(testCases):
        input = data.readline()
        (maxShy, shyness) = input.split(" ")
        noFriendsRequired = 0
        curOvation = 0
        for a in xrange(int(maxShy)+1):
            if curOvation >= a:
                curOvation += int(shyness[a])
            else:
                while curOvation < a :
                    curOvation += 1
                    noFriendsRequired += 1
                curOvation += int(shyness[a])
        print "Case #{0}: {1}".format(t+1, noFriendsRequired)
if __name__ == "__main__":
    main()