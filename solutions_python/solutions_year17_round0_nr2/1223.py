infile = open("B-large.in","r")
outfile = open("B.txt","w")
def last_nond_digit(s):
    maxi = 0
    l = len(s)
    for i in range(l):
        d = int(s[i])
        if d < maxi:
            return i - 1
        maxi = d
    return i

        
def critical_digit(s):
    last = last_nond_digit(s)
    i = 1
    last_dig = int(s[last])
    while i <= last and int(s[last-i]) == last_dig:
        i += 1
##    if int(s[last - i]) != last_dig:
##        return last - i + 1
    return last - i + 1

def solve(s):
    last = last_nond_digit(s)
    crit = critical_digit(s)
    l = len(s)
    if l <= 1:
        return s
    if last == l-1:
        return s
    
    result = s[:crit]
    if int(s[crit]) > 1:
        result += str(int(s[crit])-1)
    result += "9"*(l-crit-1)
    return result

t = int(infile.readline())
for case in range(1, t+1):
    s = infile.readline().strip()
    result = solve(s)
    outfile.write("Case #{}: {}\n".format(case, result))
infile.close()
outfile.close()
print("done")


    
