T = 0
vowels = ['a','e','i','o','u']

def main():
    caseCount = 1
    f = open('A-small-attempt0.in','r')
    o = open('outtt.out','w')
    T = int(f.readline())
    for line in f:
        name, n = line.split()
        n = int(n)
        nameLen = len(name)
        nValue = sum([consec(sub,n) for sub in substr(name,n)])
        o.write('Case #' + str(caseCount) + ': ' + str(nValue)+'\n')
        caseCount += 1
    f.close()
    o.close()

def consec(name, n):
    count = 0
    for char in name:
        if char not in vowels:
            count += 1
        else:
            count = 0
        if count >= n:
            return 1
    return 0

def substr(string,n):
    j=1
    sub=[]
    while 1:
        for i in range(len(string)-j+1):
            blah = string[i:i+j]
            if len(blah)>=n:
                sub.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
    return sub

main()
