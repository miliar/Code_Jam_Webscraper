import math

def closeScore(strscr1, strscr2):
    b1gt2 = False
    b1lt2 = False
    result1 = ''
    result2 = ''
    for i in range(len(strscr1)):
        if b1gt2 or b1lt2:
            if b1gt2 :
                if strscr1[i] == '?' and strscr2[i] == '?':
                    result1 += '0'
                    result2 += '9'
                elif strscr1[i] == '?':
                    result1 += '0'
                    result2 += strscr2[i]
                elif strscr2[i] == '?':
                    result2 += '9'
                    result1 += strscr1[i]
                else:
                    result2 += strscr2[i]
                    result1 += strscr1[i]
            if b1lt2:
                if strscr1[i] == '?' and strscr2[i] == '?':
                    result1 += '9'
                    result2 += '0'
                elif strscr1[i] == '?':
                    result1 += '9'
                    result2 += strscr2[i]
                elif strscr2[i] == '?':
                    result2 += '0'
                    result1 += strscr1[i]
                else:
                    result2 += strscr2[i]
                    result1 += strscr1[i]
        else:
            if strscr1[i] == '?' and strscr2[i] == '?':
                result1 += '0'
                result2 += '0'
            elif strscr1[i] == '?':
                result1 += strscr2[i]
                result2 += strscr2[i]
            elif strscr2[i] == '?':
                result1 += strscr1[i]
                result2 += strscr1[i]
            else:
                if strscr1[i] > strscr2[i] :
                    b1gt2 = True
                elif strscr1[i] < strscr2[i] :
                    b1lt2 = True
                result2 += strscr2[i]
                result1 += strscr1[i]
    return result1 + ' ' + result2

def rec(str1, str2):
    if str1 == "???" or str2 == '???':
        return closeScore(str1, str2)
    else:
    
        minDiff = None
        ans1 = None
        ans2 = None
        genlist1 = gen(str1)
        for str1pos in genlist1:
            genlist2 = gen(str2)
            for str2pos in genlist2:
                if minDiff == None:
                    minDiff = abs(int(str1pos) - int(str2pos))
                    ans1 = str1pos
                    ans2 = str2pos
                if minDiff > abs(int(str1pos) - int(str2pos)):
                    minDiff = abs(int(str1pos) - int(str2pos))
                    ans1 = str1pos
                    ans2 = str2pos
                if minDiff == abs(int(str1pos) - int(str2pos)):
                    if int(ans1) > int(str1pos):
                        minDiff = abs(int(str1pos) - int(str2pos))
                        ans1 = str1pos
                        ans2 = str2pos
                    elif int(ans1) == int(str1pos):
                        if int(ans2) > int(str2pos):
                            minDiff = abs(int(str1pos) - int(str2pos))
                            ans1 = str1pos
                            ans2 = str2pos
                    
        return ans1 + ' ' + ans2

def gen(strnum):
    genlist = []
    
    result = [strnum]
    while (True):
        if len(result) == 0 :
            break;
        
        num = result.pop()
        if '?' in num:
            for j in range(len(num)):
                if num[j] == '?':
                    for i in range(0,10):
                        result.append(num[:j] + str(i) + num[j+1:] )
            
        else:
            genlist.append(num)
    return genlist

f = open("B-small-attempt2(1).in", "r")

T = int(f.readline())

for x in xrange(0, T):
    readline = f.readline().strip()
    C, J = readline.split(' ')
    print "Case #" + str(x+1) + ": " + rec(C, J)
    

        