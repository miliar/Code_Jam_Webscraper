def output(s):
    #print(s)
    with open("/Users/oallbless.ctr/Documents/Google Code Jam 2017/output.out", "a") as myfile:
        myfile.write(s + "\n")

def getFlips(s, n):
    index = 0
    flips = 0
    while (index < len(s)):
        if (s[index] == '+'):
            index += 1
            continue
        if (index <= len(s) - n):
            for i in range(n):
                s[index + i] = '-' if s[index + i] == '+' else '+'
            flips += 1
        else:
            return "IMPOSSIBLE"
    
    return flips

t = int(input())
for i in range(1, t+1):
    line = input().split(' ')
    flips = getFlips(list(line[0]), int(line[1]))
    output("Case #" + str(i) + ": " + str(flips))