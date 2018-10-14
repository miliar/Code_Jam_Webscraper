import math
def main():
    fileName = 'cTest.in'
    fl = open(fileName)
    wfName = 'res' + fileName
    wf = open(wfName, 'w')
    f = fl.readline()
    f = int(f)
    res = []
    for i in range(f) :
        inter = fl.readline()
        inter = inter.split()
        [low, high] = map(int,inter)
        lowSq = int(math.sqrt(low))
        highSq = int(math.sqrt(high))
        count = 0
        #print 'case' + str(lowSq) + ' ' + str(highSq)
        for j in range(lowSq, highSq + 1) :
            if isPalindrome(j) :
                num =  j* j
                if num >= low and isPalindrome(num) :
                    count = count + 1
        res.append(count)
    j = 1
    for i in res :
        wf.write('Case #' + str(j) + ': ' + str(i) + '\n')
        j = j + 1
    
def isPalindrome(num) :
    return str(num) == str(num)[::-1]
if __name__ == "__main__" :
    main()