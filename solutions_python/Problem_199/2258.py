import  random
def flip(dlist):

    for idx in range(len(dlist)):
        if dlist[idx] == '+':dlist[idx] = '-'
        else :dlist[idx] = '+'
    return dlist

def flipper(string,k):
    totalLen = len(string)
    strList = list(string)
    count = 0
    while strList.count('-')>0:
        pointer = strList.index('-')
        if pointer > totalLen-k:
            return "IMPOSSIBLE"
        subList= strList[pointer:pointer+k]
        subList = flip(subList)
        strList = strList[:pointer]+subList+strList[pointer+k:]
        count+=1

    return  count
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
        ip  = input().split()
        string = ip[0]
        k = int(ip[1])
        ans = flipper(string,int(k))
        print('Case #%d:'%(idx+1) +' '+str(ans))
if __name__ == '__main__':
    main()

