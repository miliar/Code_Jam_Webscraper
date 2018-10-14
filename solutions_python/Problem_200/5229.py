# fr = open("B-small.in", "r")
# fw = open("B-small.out", "w+")
# cases = int(fr.readline())

cases = int(raw_input())

def checkNonDecreasing(num):
    s = str(num)
    return all(s[i] <= s[i+1] for i in range(len(s) - 1))

for i in range(cases):
    #num = int(fr.readline())
    num = int(raw_input())
    if num / 10 == 0:
        print "Case #" + str(i + 1) + ": " + str(num)
        #fw.write("Case #" + str(i + 1) + ": " + str(num)+"\n")
    else:
        while True:
            if checkNonDecreasing(num):
                break
            num -= 1
        print "Case #" + str(i + 1) + ": " + str(num)
        #fw.write("Case #" + str(i + 1) + ": " + str(num)+"\n")

# fr.close()
# fw.close()