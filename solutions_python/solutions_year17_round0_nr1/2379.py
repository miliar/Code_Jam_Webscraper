
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
    # call the function with the arguments
    result = solution(list(s[0]), int(s[1]))
    print("Case #" + str(i + 1) + ": " + str(result))
    # store the result 
    # print Case #i: str(result)