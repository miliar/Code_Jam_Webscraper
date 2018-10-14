def check(s):
    for c in s:
        if c == '-':
            return False
    return True

def flip(s, n):
    
    
    for i in range(len(s)):
        if s[i] == '-':
            if i+n > len(s):
                return 0
            for j in range(n):
                if s[i+j] == '-':
                    s[i+j] = '+'
                else:
                    s[i+j] = '-'
                
            return s

infile = open("A-large.in", "r")
outfile = open("A-large.out", "w")

t = infile.readline()
print(t)
casenumber = 1
for line in infile:
    count = 0
    s, n = line[:-1].split()
    print(s, n)
    n = int(n)
    s = list(s)

    while not check(s):
        s = flip(s, n)
        
        if s == 0:
            count = "IMPOSSIBLE"
            break
        count += 1
        
    print("Case #{}: {}".format(casenumber, count), file=outfile)
    casenumber+=1
print("done")
infile.close()
outfile.close()
