import logging
import numpy as np
import random

def countingSheep(filename='inputA.in'):
    #reader
    rownum = 0
    numbers = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                numbers.append(int(row))
            rownum += 1
    logging.debug('List of numbers: ' + str(numbers))
    
    #algo
    solList = list()
    for e in numbers:
        if e == 0:
            solList.append('INSOMNIA')
            continue
        currentNumber = e
        check = [0,1,2,3,4,5,6,7,8,9]
        while check:
            logging.debug('BEFORE: Current number: ' + str(currentNumber) + '\tChecklist: ' + str(check))
            digits = [int(x) for x in str(currentNumber)]
            removables = list()
            for f in check:
                if f in digits:
                    removables.append(f)
            for f in removables:
                check.remove(f)
            logging.debug('AFTER: Current number: ' + str(currentNumber) + '\tChecklist: ' + str(check))
            currentNumber += e
        solList.append(str(currentNumber-e))

    #writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(solList)):
            file.write('Case #' + str(i+1) + ': ' + solList[i] + '\n')
    

def pancakes(filename='inputB.in'):
    #reader
    rownum = 0
    stacks = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                stack = list()
                for e in row.strip():
                    if e == '+':
                        stack.append(1)
                    else: # e == '-'
                        stack.append(-1)
                stacks.append(stack)
            rownum += 1
    logging.debug('List of stacks: ' + str(stacks))

    #algo
    solList = list()
    for stack in stacks:
        n = 0
        while True:
            logging.debug('n: ' + str(n))
            logging.debug('Stack: ' + str(stack))
            while stack and stack[-1]==1:
                stack = stack[0:-1]
            if not stack:
                break
            logging.debug('Stack after pruning: ' + str(stack))
            if stack[0] == -1:
                stack = [ e * -1 for e in list(reversed(stack))]
            else:
                i = 0
                while stack[i] == 1:
                    stack[i] = -1
                    i += 1
            n += 1
            logging.debug('Stack after operation: ' + str(stack))
        solList.append(n)
        logging.debug('Final n: ' + str(n))

    #writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(solList)):
            file.write('Case #' + str(i+1) + ': ' + str(solList[i]) + '\n')


def jamcoin(filename='inputC.in'):

    #reader
    rownum = 0
    Js = list()
    Ns = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                row = row.split(' ')
                Js.append(int(row[1]))
                Ns.append(int(row[0]))
            rownum += 1

    #algo
    overallSol = list()
    for i in range(len(Js)):
        J = Js[i]
        N = Ns[i]
        solList = list()
        coinJamList = list()

        while len(solList) < N:
            jam = generateJam(J, coinJamList)
            divList = list()
            for b in range(2,11):
                num = convertBasis(jam, b)
                logging.debug('real number: ' + str(num))
                div = findDiv(num)
                if div == -1:
                    break
                else:
                    divList.append(div)
            logging.debug('List of divisors: ' + str(divList))
            if len(divList)==9:
                divList.insert(0,int(jam))
                logging.debug('divList: ' + str(divList))
                solList.append(divList)
            logging.debug('Sol list: ' + str(solList))
        overallSol.append(solList)
    logging.debug('Overall soluton: \n' + str(overallSol))

    #writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(overallSol)):
            file.write('Case #' + str(i+1) + ':\n')
            for j in range(len(overallSol[i])):
                for e in overallSol[i][j]:
                    file.write(str(e) + ' ')
                file.write('\n')


def convertBasis(jam, b):
    a = 0
    p = 0
    for i in range(len(jam)-1,-1,-1):
        a += int(jam[i])*(b**p)
        p += 1
    return a

def findDiv(n):
    k = 2
    while k <= int(n**0.5)+1 and k <= 1000:
        if n%k==0:
            return k
        k += 1
    return -1

def generateJam(J, coinJamList):
    flag = True
    while flag:
        s = ''
        for i in range(J-2):
            s += str(random.randint(0,1))
        s = '1' + s + '1'
        if not s in coinJamList:
            flag = False
            coinJamList.append(s)
    logging.debug('generated jam: ' + s)
    return s

def pancake(filename='inputA.in'):
    #reader
    rownum = 0
    v = list()
    k = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                srow = row.split()
                vTmp = list()
                for l in srow[0]:
                    # print(l)
                    if l == 43:
                        vTmp.append(1)
                    else:
                        vTmp.append(-1)
                v.append(vTmp)
                k.append(int(srow[1]))
            rownum += 1
    logging.debug('first v: ' + str(v[0]))
    logging.debug('first k: ' + str(k[0]))
    
    #writer
    f = open('Output/' + filename.split('.')[0] + '.out', 'w')
    
    #algo
    for i in range(len(v)):
        vIter = v[i]
        kIter = k[i]

        count = 0
        for j in range(len(vIter)-kIter+1):
            if vIter[j] == -1:
                # print(vIter)
                for a in range(j, j+kIter):
                    vIter[a] *= -1
                # print(vIter)
                count += 1

        # test
        if sum(vIter) == len(vIter):
            f.write('Case #' + str(i+1) + ': ' + str(count) + '\n')
        else:
            f.write('Case #' + str(i+1) + ': IMPOSSIBLE\n')

def tinyNumbers(filename='inputB.in'):
    #reader
    rownum = 0
    vList = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                vList.append(list(str(int(row))))
            rownum += 1
    logging.debug('first v: ' + str(vList[0]))

    f = open('Output/' + filename.split('.')[0] + '.out', 'w')
    #algo
    for i in range(len(vList)):
        v = vList[i]
        # print(len(v))
        for j in range(len(v)-1, 0, -1):
            print(v)
            if v[j] < v[j-1]:
                v[j] = '9'
                v[j-1] = str(int(v[j-1])-1)

                jIter = j + 1
                while jIter < len(v):
                    v[jIter] = '9'
                    jIter += 1

        
        f.write('Case #' + str(i+1) + ': ')
        for j in v:
            if j != '0':
                f.write(j)
        f.write('\n')


def bathroom(filename='inputC.in'):
    #reader
    rownum = 0
    nList = list()
    kList = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                row = row.split()
                nList.append(int(row[0]))
                kList.append(int(row[1]))
            rownum += 1
    logging.debug('first n: ' + str(nList[0]))
    logging.debug('first k: ' + str(kList[0]))

    # algo
    f = open('Output/' + filename.split('.')[0] + '.out', 'w')
    for i in range(len(nList)):
        n = nList[i]
        k = kList[i]
        
        # init datastructure
        d = [{'leftB' : 0, 'rightB' : n-1, 'maxminVal' : int((n-1)/2), 'maxminIdx' : int((n-1)/2), 'maxmaxVal' : int((n)/2)}]
        kCount = 1
        while(True):
            print('Iteration: ' + str(i))
            # print('Iteration: ' + str(i) + ': ' + str(d))
            # find max element
            maxEle = d.pop(-1)
            if kCount == k:
                f.write('Case #' + str(i+1) + ': ' + str(maxEle['maxmaxVal']) + ' ' + str(maxEle['maxminVal']) + '\n')
                break
                
            # call subfunction
            dL, dR = bathroomSub(maxEle)
            # insert new intervalls
            d = bathroomInsert(d, dL)
            d = bathroomInsert(d, dR)
            kCount += 1
        
def bathroomInsert(dList, d):
    if not dList:
        return [d]
    for i  in range(len(dList)):
        e = dList[i]
        if ((d['maxminVal'] < e['maxminVal']) or 
            ((d['maxminVal'] == e['maxminVal']) and (d['maxmaxVal'] < e['maxmaxVal'])) or
            ((d['maxminVal'] == e['maxminVal']) and (d['maxmaxVal'] == e['maxmaxVal']) and (d['maxminIdx'] > e['maxminIdx']))):
            dList.insert(i, d)
            return dList
    dList.append(d)
    return dList

def bathroomSub(d):
    # print('\t' + str(d))
    # left
    l = d['leftB']
    r = d['maxminIdx']-1
    dL = {'leftB' : l,
          'rightB' : r,
          'maxminVal': int((r-l)/2),
          'maxminIdx': int((l+r)/2),
          'maxmaxVal': int((r-l+1)/2)
         }
    # right
    l = d['maxminIdx']+1
    r = d['rightB']
    dR = {'leftB' : l,
          'rightB' : r,
          'maxminVal': int((r-l)/2),
          'maxminIdx': int((l+r)/2),
          'maxmaxVal': int((r-l+1)/2)
         }
    # print('\t' + str(dL))
    # print('\t' + str(dR))
    return [dL, dR]



if __name__ == "__main__":

    FORMAT = '%(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    # countingSheep('inputLargeA.in')
    # pancakes('inputLargeB.in')
    # jamcoin('inputC.in')
    # pancake('inputA.in')
    # tinyNumbers('inputB.in')
    bathroom('inputC.in')












