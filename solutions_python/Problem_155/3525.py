#!/usr/bin/python
def main() :
    fobj = open("smallinput", 'r')
    writeobj = open("output.txt", 'w')
    caseNum = int(fobj.readline())
    print("No of cases is %d" %caseNum)
    i = 0
    for i in range (0, caseNum) :
        list1 = fobj.readline().split('\n')[0].split(' ')
        maxshy = int(list1[0])
        standing = 0
        need = 0
        # Can be upto 1000 digits long
        countstr = str(list1[1])
        for shy in range (0, len(countstr)) :
            if int(countstr[shy]) == 0:
                continue
            if standing > maxshy:
                break
            if standing < shy:
                need = need + (shy - standing)
                # keep going
                standing = standing + need
            standing = standing + int(countstr[shy])

        print("maxshy is %d, need is %d" %(maxshy, need))
        writeobj.write("Case #%d: %d\n" %(i+1, need))

    writeobj.close()
    fobj.close()

main()
