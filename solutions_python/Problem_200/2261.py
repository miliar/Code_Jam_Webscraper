def isTidy(n):
    c = n % 10 # get the digit
    n = n // 10 # remove digit
    
    while(n != 0):
        cc = n % 10 # get the digit
        n = n // 10 # remove digit
        if( cc <= c ):
            c = cc

        else:
            return False

    return True

def solution():
    n = int(input())
    for i in range(n, 0, -1):
        if( isTidy(i) ):
            return i


testcases = int(input())
for i in range(testcases):
    print("Case #" + str(i+1) + ": " + str(solution()))
