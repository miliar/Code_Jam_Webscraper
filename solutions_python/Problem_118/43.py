import math

def isSquareFair(x):
    x = x * x
    i = 10
    while i <= x:
        i *= 10
        
    i /= 10
    j = 10
    
    while i >= j:
        if ((x % (i * 10)) / i) != ((x % j) / (j / 10)):
            return 0
        
        i /= 10
        j *= 10
    
    return 1
    
    
def getLength(n):
    i = 1
    while n > pow(10, i):
        i += 1
    return i
    
def getPalindromeNum(n):
    i = getLength(n) / 2
    return n / pow(10, i) * pow(10, i + 1) + n % pow(10, i + 1)


def insertPalindromeNum(n, c):
    i = getLength(n) / 2
    return n / pow(10, i) * pow(10, i + 1) + c * pow(10, i) + n % pow(10, i)
  
 
def printList(list):
    tmp = " "
    for n in list:
        tmp = tmp + " %s : " % (n)
        
    print tmp
      
def init():

    result_list = [1, 2, 3, 11, 22]
    tmp_result = [11, 22] 
    
    for len in range(55):
        new_result = []
        for num in tmp_result:
            if len % 2 == 1:
                new_num = getPalindromeNum(num)
                if isSquareFair(new_num) == 1:
                    new_result.append(new_num)
            else:
                for i in range(3):
                    new_num = insertPalindromeNum(num, i)
                    if isSquareFair(new_num) == 1:
                        new_result.append(new_num)
            
        result_list.extend(new_result) # append all elements from new_result to result_list
        tmp_result = new_result  # copy new_result to tmp_result
        
    #print(result_list)
    
    result_list = [x * x for x in result_list] 
    return result_list
        
total = input()
result_list = init()

for index in range(total):
    count = 0
    A, B = map(long, raw_input().split())
    
    ans = 0
    for n in result_list:
        if n >= A and n <= B:
            ans += 1
        elif n > B:
            break
    
    result = "Case #%s: %s" % (index + 1, ans)
    print result

