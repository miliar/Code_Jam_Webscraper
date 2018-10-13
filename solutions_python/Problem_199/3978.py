import copy
import sys

def checkStr(s,sign):
    for i in s:
        if i != sign:
            return False
    return True

def processStr(s,k):
    c1 = 0
    s1 = copy.deepcopy(s)
    s2 = copy.deepcopy(s)
    for idx in range(len(s1)-k+1):
        if s1[idx] == '-':
            for jdx in range(idx,idx+k):
                if s1[jdx] == "-":
                    s1[jdx] = "+"
                else:
                    s1[jdx] = "-"
            c1 += 1
    #print s1
    flag = checkStr(s1,"-")
    if flag == False:
        c1 = 100000
    
    c2 = 0
    for idx in range(len(s2)-k+1):
        if s2[idx] == '-':
            for jdx in range(idx,idx+k):
                if s2[jdx] == "-":
                    s2[jdx] = "+"
                else:
                    s2[jdx] = "-"
            c2 += 1
    #print s2
    flag = checkStr(s2,"+")
    '''
    print "----"
    print c1,c2
    print "----"
    '''
    if flag == False:
        c2 = 100000
    return min([c1,c2])

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'a+')
    t = int(raw_input())
    case = 0
    while t>0:
        case = case+1
        s,k = raw_input().split()
        s = list(s)
        k = int(k)
        count1 = processStr(s,k)
        s = s[::-1]
        count2 =  processStr(s,k)
        #print count1,count2
        count =  min([count1,count2])
        if count != 100000:
            print "Case #{}: {}".format(case,count)
        else:
            print "Case #{}: IMPOSSIBLE".format(case)
        t -= 1

if __name__ == "__main__":
    main()
