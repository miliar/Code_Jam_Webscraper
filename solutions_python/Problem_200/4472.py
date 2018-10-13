def removePaddingZeros(num):
    j = 0
    while num[j]=='0':
        j+=1
    #print "".join(num[j:])
    return "".join(num[j:])
def cleanup(num,i):
    j = i-1
    while j>=0:
        if num[j] > num[j+1]:
            num[j+1] = '9'
            num[j] = chr(ord(num[j])-1)
        j-=1

def findLastTidyNumber(num):
    i = 0
    while i < len(num)-1:
        if num[i]>num[i+1]:
            num = num[0:i]+ [chr(ord(num[i])-1)]+['9' for i in range(i+1,len(num))]
            cleanup(num,i)

            break
            #Traverse down to get the rest
        i+=1
    return removePaddingZeros(num)

def main():
    n = int(raw_input())
    case = 0
    while n > 0:
        n -= 1
        case += 1
        number = list(raw_input())
        print "Case #"+ str(case)+": "+ findLastTidyNumber(number)


if __name__=='__main__':
    main()
