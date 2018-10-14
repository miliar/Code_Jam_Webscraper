def get_count(A,B):
    result = 0
    a = len(A)
    b = len(B)
    list = set()
    sqlist = set()
    for num in range(1,b+1):
        list = list.union(GetPalindrome(num))
    for num in list:
        t = int(num)
        sqlist.add(t*t)
    for num in sqlist:
        if num >= int(A) and num <= int(B) and str(num) in list:
            result = result +1
    return str(result)

def GetPalindrome(number):
    result = []
    num = ['1' for i in range(number)]     
    return nextNum(num)

def nextNum(num,index=0):
    if index >= len(num)/2+1:
        return set()
    else:
        result = set()
        for i in range(0,10):
            if i==0 and index == 0:
                continue
            else:
                num[index] = str(i)
                num[-(index+1)] = str(i)
                number = ''.join(num)
                result.add(number)
                result = result.union(nextNum(num,index+1))
        return result


num = raw_input()
for i in range(0,int(num)):
    A_B = raw_input()
    A_B = A_B.split(' ')
    A = A_B[0]
    B = A_B[1]
    print 'Case #'+str(i+1)+': '+get_count(A,B)
    