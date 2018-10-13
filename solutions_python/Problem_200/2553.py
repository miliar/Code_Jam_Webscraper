

# function to flip 
def flip(s):
    if s == '+' :
        return '-'
    else:
        return '+'

# function takes N as input and prints output

def compare(f, s):
    return int(f) < int(s)

def solution(N):
    
    result = None 
    n = list(str(N)) 
    i = len(n) - 1 

    while i > 0 :

        # print(i, len(n))
        if compare(n[i], n[i-1]):
            # do something 
            # change i, i -1
            f = int(n[i -1])
            # s = int(n[i])
            # change i+1 till end with 999
            n[i-1] = str(f - 1)
            n[i] = "9"
            n = n[:i + 1] + list("9" * (len(n) - (i + 1)) )
        else:
            i-=1

    
    k = ''.join(n)
    if k[0] == '0':
        result = k[1:]
    else:
        result = k
    return result

# brute force check :P 
# def check(N):

#     n = list(str(N))

#     result = True

#     i = len(n) - 1
#     while i > 0:
#         if compare(n[i], n[i - 1]):
#             result = False
#             break
#         i-=1
    
#     return result

# def solution_b(N):

#     while not check(N):
#         N-=1
    
#     return N

n = int(raw_input())
for i in range(n):
    # pass
    # read the inout number
    N = int(raw_input())
    result = solution(N)
    print("Case #" + str(i + 1) + ": " + str(result))
    # print Case #i: str(result)