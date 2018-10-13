def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = [s for s in raw_input().split(" ")]  # read a list of one integer
        n = n[0]
        n = list(n)

        pointer = 0
        listLength = len(n)

        k = 1
        while k < listLength:
            while pointer+1 <= listLength-k:
                thisNumber = int(n[pointer])
                nextNumber = int(n[pointer + 1])
                if nextNumber<thisNumber:
                    thisNumber-=1
                    for j in range(pointer+1, listLength):
                        n[j] = '9'
                    n[pointer] = str(thisNumber)
                    if thisNumber==0 and pointer==0:
                        n.pop(pointer)
                        listLength-=1
                pointer += 1
            pointer = 0
            k+=1
        print "Case #{}: {}".format(i, ''.join(list(n)))
        # check out .format's specification for more formatting options

main()