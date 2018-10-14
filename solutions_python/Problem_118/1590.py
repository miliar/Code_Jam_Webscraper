def make(i):
    s = str(i)
    t = s[::-1]
    s = s + t
    return int(s)
    
def make1(i):
    s = str(i)
    t = s[::-1]
    s = s + t[1:len(t)]
    return int(s)
    

def ispal(s):
    t = str(s)
    for i in range(0, len(t) // 2):
        if t[i] != t[len(t) - i - 1]:
            return 0
    return 1

def to3(i):
    x = "";
    while i > 0:
        x +=str (i % 3)
        i //= 3
    return x[::-1]
    
def main():
    input = open('C-large-1.in', 'r')
    output = open ('output.txt', 'w')
    s = input.readlines()
    t = []
    for i in range(1, len(s)):
        l = int(s[i].split(' ')[0])
        r = int(s[i].split(' ')[1])
        t.append( [l, r, 0])
    q = [0, 0]
    for j in range (1, 1000):
        x = int(to3(j))
        temp = make(x)*make(x)
        q += [temp]
        temp = make1(x)*make1(x)
        q += [temp]
    for i in t:
        for j in range (1, 1000):
            temp = q[j * 2]
            if ispal(temp):
                if (temp >= i[0] and temp <= i[1]):
                    i[2]+=1
            temp = q[j*2+1]
            if ispal(temp):
                if (temp >= i[0] and temp <= i[1]):
                    i[2]+=1
        if (i[0]<=9 and i[1] >=9):
            i[2] += 1
    for i in range(0, len(t)):
        output.write("Case #" + str(i + 1) + ": " + str(t[i][2]) + '\n')
        

if __name__ == '__main__':
    main()   