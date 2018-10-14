reader = file("A-small-attempt0.in")
# skip first line with use case number
line = reader.next()

def consecutive_constans(s):
    max = 0
    temp = 0
    for i in range(0,len(s)):
        if not (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            temp = temp + 1
        else:
            if max < temp:
                max = temp
            temp = 0
    if max < temp:
        max = temp
    #print max
    return max

def process_case(case, name, n):
    nvalue = 0
    #print "n: " + str(n)
    for i in range(0,len(name)):
        for j in range(i+1,len(name)+1):
            cc = consecutive_constans(name[i:j])
            #print name[i:j]
            #print cc
            if (cc >= n):
                nvalue = nvalue + 1
    print "Case #" + str(case) + ": " + str(nvalue)

i = 1
for line in reader:
    l = line.split()
    process_case(i, l[0], int(l[1]))
    i = i + 1