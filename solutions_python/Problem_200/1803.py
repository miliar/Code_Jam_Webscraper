


def readData(input_file):
    f=open(input_file)
    numCase=int(f.readline())
    #print numCase
    numb = []
    for i in range(numCase):
        line = f.readline()
        numb.append(int(line))
    #print numb[3]
    return numCase, numb

def smallestSorted(n):
    if str(n) == ''.join(sorted(str(n))):
        return n
    elif n<int('1'*len(str(n))):
        return int('9'*(len(str(n))-1))
    else:
        s = str(n)
        t = ['9'] * len(str(n))
        for i in range(len(str(n))-1):
            if s[i] > s[i+1]:
                for j in range(i):
                    t[j] = s[j]
                t[i] = str(int(s[i])-1)
                for j in range(len(t)-1,0,-1):
                    if t[j] < t[j-1]:
                        t[j] = '9'
                        t[j-1] = str(int(t[j-1]) - 1)
                return ''.join(t)
    
input_file="B-large.in"
numCase,numb  = readData(input_file)
for i in range(numCase):
    ans = smallestSorted(numb[i])
    print 'Case #'+str(i+1)+': '+str(ans)
