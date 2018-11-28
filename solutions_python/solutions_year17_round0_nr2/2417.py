import  random
def flip(dlist):

    for idx in range(len(dlist)):
        if dlist[idx] == '+':dlist[idx] = '-'
        else :dlist[idx] = '+'
    return dlist

def flipper(string):
    totalLen = len(string)
    if totalLen == 1:
        return int(string)
    strList = list(string)


    pointer = 0

    idx =0
    while int(strList[idx+1]) >= int(strList[idx]):
        if idx+1 ==  totalLen-1:
            return int(string)
            break
        idx+=1
        pointer+=1

    temp = pointer

    if pointer >0:

        while strList[temp] == strList[temp-1]:
            if temp == 0:
                break
            temp-=1

    strList = strList[:temp]+ [str(int(strList[temp])-1)] + ['9']*(len(strList[temp:])-1)

    return  int("".join(strList))
def main():
    size =10
    ans = 'IMPOSSIBLE'
    strlist =''
    '''
    while ans == 'IMPOSSIBLE':
        string = ''
        charac = ['+','-']

        for i in range(size):
            idx = random.randint(0,1)
            string+=charac[idx]
        #string = '---+-++-'
        print(string)
        ans = flipper(string,6)
        print(ans)
    #print(strlist)
    '''
    testCase = int(input())
    for idx in range(testCase):
        #ip  = input().split()
        string = input()

        ans = flipper(string)
        print('Case #%d:'%(idx+1) +' '+str(ans))
if __name__ == '__main__':
    main()

