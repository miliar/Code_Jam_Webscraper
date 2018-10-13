
def isTidy(t):
    potential_tidy = str(t)
    if len(potential_tidy) == 1:
        return True
    else:
        prev = 0
        for i in range(0,len(potential_tidy)):
            if int(potential_tidy[i]) < prev:
                return False
            else:
                prev = int(potential_tidy[i])
    return True

def checkTidy(N):
    tidy = 0
    if N < 1000000:
        i = 1
        while i < N+1:
            if isTidy(i):
                tidy = i
            i += 1
    else: # when N > 10^7
        i = N-(N/2)

    return tidy


with open("B-small-attempt0.in", "r") as f:
    lines = f.readlines()
    T = int(lines[0])
    x = 1
    result = ""
    while (x < T+1):
        # toys : smallest -> largest
        # pencils : shortest -> longest
        # computers : oldest -> newest

        # int written in base 10 with no leading zeroes
        # have their digits sorted in non-decreasing order        
        N = int(lines[x])
        y = checkTidy(N)
        result += "Case #" + str(x) + ": " + str(y) + "\n"        
        x+=1

    print(result)
    file = open("output.o","w") 
    file.write(result)
    file.close()
