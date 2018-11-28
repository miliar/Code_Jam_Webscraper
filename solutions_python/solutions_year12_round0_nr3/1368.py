from collections import deque

def zeropad(inNum,leng):
    zeros = ''
    for i in range (leng - len(str(inNum))):
        zeros += '0'

    #print zeros+str(inNum)
    return zeros + str(inNum)

def moveOneNum(inNumStr):
    #from the back to the front
    output = inNumStr[len(inNumStr)-1] + inNumStr[:-1]
    return int(output)

def MainFunction( inStr) :
    inputL = inStr.split(' ')
    count=0
    for n in range( int(inputL[0]),int(inputL[1])+1):
        #print n
        oldchanged = n
        for j in range(len(str(n))):
            #print j
            newchanged = moveOneNum(zeropad(oldchanged,len(str(n))))
            #print 'compare: ' + str(n)  + ' < ' + str(newchanged)
            if(n < newchanged and newchanged <= int(inputL[1])): #and len(str(newchanged)) == len(str(n)) 
                #print 'true!!!!!!!!!!!!!!!!!!!' + str(count)
                answer = '(' + str(n) + ',' + str(newchanged) +')'
                if (answer not in answerQueue):
                    answerQueue.append(answer)
                    answerQueue.popleft()
                    count += 1
                
            oldchanged = newchanged

    output = ""
    print count
    return str(count)


f=open('E:\\Dropbox\\2012-project\\GoogleJam\\C-large.in')
fw = open('E:\\Dropbox\\2012-project\\GoogleJam\\C-large.out','w')

answerQueue = deque([0,0,0,0,0,0,0,0,0,0])
numberLines = int(f.readline())

for x in range(numberLines):
    output = "Case #" +str(x+1)+": " + MainFunction(f.readline()) +'\n'
    fw.write(output)

f.close()
fw.close()

