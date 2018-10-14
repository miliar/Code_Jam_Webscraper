# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def pancakes(string, n):
    if (n > len(string)):
        return "IMPOSSIBLE"
    allHappy = False;
    flips = 0
    firstItr = True
    firstChange = string
    while (not allHappy):
        happies = 0
        for i in range(0,len(string)):
            if (string[i] == '+'):
                happies += 1
            if (string[i] == '-'):
                flips += 1
                if (i >= len(string) - n):
                    string = string[0:len(string) - n] + flip(string[len(string) - n:len(string)])
                    if (string == firstChange):
                        return "IMPOSSIBLE"
                    if (firstItr):
                        firstChange = string
                        firstItr = False
                else:
                    string = string[0:i] + flip(string[i:i+n]) + string[i+n:len(string)]
                    if (string == firstChange):
                        return "IMPOSSIBLE"
                    if (firstItr):
                        firstChange = string
                        firstItr = False
                i = len(string)
        if (happies == len(string)):
            allHappy = True
        if (flips > len(string)):
            return "IMPOSSIBLE"
                
    return flips

def flip(string):
    new = ''
    for i in range(0,len(string)):
        if (string[i] == '+'):
            new += '-'
        else:
            new += '+'
    return new
            


t = int(input())
for i in range(1, t + 1):
    inputS = input().split(" ")
    s = inputS[0]
    n = int(inputS[1]) 
    print("Case #{}: {}".format(i, pancakes(s, n)))
  
          
