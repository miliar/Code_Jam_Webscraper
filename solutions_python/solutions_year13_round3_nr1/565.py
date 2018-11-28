def nValue(nomen, n):
    binary = turnBinary(nomen)
    print(binary)
    return recursiveTrace(binary, n)

def turnBinary(s):
    binary = ""
    for i in range(len(s)):
        if s[i] in "aeiou":
            binary += "0"
        else:
            binary += "1"
    return binary


# wish i could binary.split('0')
def recursiveTrace(binary, n):
    # returns number of substrings etc.
    if len(binary) < n:
        return 0
    if ("1"*n) in binary:
        return 1 + recursiveTrace(binary[:-1], n) + leftwardsTrace(binary[1:], n)
    else:
        return 0

def leftwardsTrace(binary, n):
    # returns substrings shrinking toward right
    if len(binary) < n:
        return 0
    if ("1"*n) in binary:
        return 1 + leftwardsTrace(binary[1:], n)
    else:
        return 0

########################################

name = raw_input().replace(".in", "")

f = open(name+".in", 'r')
g = open(name+".out", 'w')

cases = int(f.readline())

for i in range(cases):
    values = f.readline().split()
    a = str(values[0])
    b = int(values[1])
    
    g.write("Case #%d: %d\n" % (i+1, nValue(a, b)))

    
f.close()
g.close()
