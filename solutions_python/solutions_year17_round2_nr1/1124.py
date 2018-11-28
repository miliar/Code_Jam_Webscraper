
# function to flip 
def flip(s):
    if s == '+' :
        return '-'
    else:
        return '+'

# function which takes string, k as input and outputs result
def solution(s, k):

    count = 0
    i = 0
    l = len(s)
    while i < l :
        if s[i] == '-' :
            # do something 
            if i + k > l:
                return "IMPOSSIBLE"
            else:
                for c in range(i, i + k):
                    s[c] = flip(s[c])
                count+=1 
        
        i+=1


    return count

n = int(raw_input())
for i in range(n):
    # pass
    # read the inout string
    s = str(raw_input())
    # split it 
    s = s.split(' ')
    # print(s)
    D = float(s[0])
    K = int(s[1])
    maxt = 0
    for j in range(K):
        t = str(raw_input())
        t = t.split()
        maxt = max(maxt, (D - float(t[0]))/float(t[1]) )
    
    # call the function with the arguments
    result = round(D / maxt, 6)
    print("Case #" + str(i + 1) + ": " + "{0:6f}".format(result))
    # store the result 
    # print Case #i: str(result)