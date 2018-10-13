import os
import time
from functools import reduce

t1 = time.time()

def isPalin(n):
        return str(n) == str(n)[::-1]

def updateInserts():
        global inserts
        global inserts_last
        global lenIns
        
        temp = inserts
        if lenIns == 1:
                inserts = ['00', '11', '22']
        else:
                inserts = []
                for i in inserts_last:
                        inserts.append('0' + i + '0')
                        inserts.append('1' + i + '1')
                if lenIns == 2:
                        inserts_last = ['00','11']
                else:
                        inserts_last = temp
        lenIns = len(inserts[0])

inHandle = open('input.txt','r')
outHandle = open('output.txt','w')

inserts_last = ['0','1','2']
inserts = ['0','1','2']
lenIns = 1
tenH = 10 ** 100

solutions = [1,4,9,121,484]

nCases = int(inHandle.readline().replace('\n',''))
go = True
while(go):
        print(lenIns)
        base = '11'
        for i in inserts:
                if(i.find('111111111') == 0):
                        continue
                n = '1' + i + '1'
                square = int(n)**2
                if(square <= tenH and isPalin(square)):
                        solutions.append(square)
                elif(square > tenH):
                        go = False
                        break
        twos = []
        if(lenIns == 1):
                twos=['202','212']
        elif(lenIns % 2 == 0):
                twos.append('2' + reduce(lambda x,y:x+y, list('0' * lenIns)) + '2')
        else:
                half = int(lenIns/2)
                twos.append('2' + reduce(lambda x,y:x+y, list('0' * lenIns)) + '2')
                twos.append('2' + reduce(lambda x,y:x+y, list('0' * half)) + '1' + reduce(lambda x,y:x+y, list('0' * half)) + '2')
        for tt in twos:
                square = int(tt)**2
                if(square <= tenH and isPalin(square)):
                        solutions.append(square)
                elif(square > tenH):
                        go = False
                        break
        updateInserts()

sorted_solutions = sorted(set(solutions))

for case in range(nCases):
        givenRange = inHandle.readline().split(' ')
        low = int(givenRange[0])
        high = int(givenRange[1])
        answer = 0
        for i in sorted_solutions:
                if i < low:
                        continue
                if i > high:
                        break
                else:
                        answer = answer + 1

        outHandle.write('Case #' + str(case+1) + ': ' + str(answer) + '\n')

inHandle.close()
outHandle.close()

print("finished in ", time.time() - t1, " seconds")
