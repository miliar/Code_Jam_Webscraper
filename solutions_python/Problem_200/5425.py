# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

       
def tidy(x):
    tidy = True
    while x>0:
        tidy = (x//10)%10 <= x%10
        x = x//10
        if not(tidy):
            return tidy
    return tidy

def last_tidy(N):
    if N//10 ==0:
        return N
    else:
        for x in range(N,10, -1):
            if tidy(x):
                return(x)

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):

    try:
        N = int(input().split(" ")[0])  # read an integer
        print("Case #{}: {} ".format(i, last_tidy(N)))

        
        #    print(str(x) + ' ' + str(tidy(x)))
        
    except Exception as e:
        print(e)
