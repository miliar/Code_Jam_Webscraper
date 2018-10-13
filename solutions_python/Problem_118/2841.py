import math

#upper_limit = 10**7
upper_limit = 10**4
palindrome_list = [False]*(upper_limit+1)
both_true = [0]*(upper_limit**2+1)
#print both_true
#for i in range(1,10**7+1) :

for i in range(1,upper_limit+1):
    to_check = str(i)

    strlen = len(to_check)
    is_palindrome = True
    for j in range(strlen/2) :
        if j >= strlen-1-j :
            break
        if to_check[j] != to_check[strlen-1-j] :
            is_palindrome = False
            break

    if is_palindrome :
        palindrome_list[i] = True
for i in range(1,upper_limit+1) :
    square = i*i
    to_check = str(square)

    strlen = len(to_check)
    is_true_palindrome = True
    for j in range(strlen/2) :
        if j >= strlen-1-j :
            break
        if to_check[j] != to_check[strlen-1-j] :
            is_true_palindrome = False
            break

    if is_true_palindrome and palindrome_list[i] :
        #print "%d is  palindrome"%(i*i,)
        both_true[i*i] = 1 



#check with dynamic programming
addendum = [0]*(10**7+1)

for i in range(1,upper_limit+1) :
    addendum[i] = addendum[i-1]+both_true[i]
    #print "%d-> %d"%(i,addendum[i])


T = int(raw_input())

for t in range(1,T+1) :
    limit = raw_input().split()
    limit = [int(entry) for entry in limit ]
    #print limit
    #print addendum[limit[1]] - addendum[limit[0]-1
    print "Case #%d: %d"%(t,addendum[limit[1]] - addendum[limit[0]-1])
