def incOrder(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
    return True
    
def findLast(n):
    if len(n) == 1:
        return n
    list_n = map(int,list(n))
    while(not incOrder(list_n)):
        first = False
        for i in range(1,len(n)):
            if list_n[i] < list_n[i-1]:
                if first == False:
                    list_n[i-1] -= 1
                    first = True
                list_n[i] = 9
    return "".join(map(str,list_n)).lstrip("0")
    
def altFindLast(n):
    num = int(n)
    while(not incOrder(str(num))):
        num -= 1
    return num
    
l = int(raw_input())
for x in range(l):
    p = raw_input()
    print "Case #"+str(x+1)+": "+findLast(p)
    

