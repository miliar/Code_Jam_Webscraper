
def flip(c):
    if c == "+":
        return '-'
    elif c == "-":
        return "+"


stack = []
visited = []


def flipper(stack, k):
    count = stack[0][1]
    s = stack[0][0]
    if s.count("-") == 0:
        stack.pop(0)
        return count
    for i in range(len(s)):
        if s[i] == "-":
            for h in range(k):
                pos = i - k + 1 + h
                if pos < 0 or (pos + k) > len(s):
                    continue
                tempStr = s[:pos]
                for j in range(k):
                    tempStr += flip(s[pos+j])
                tempStr += s[pos+k:]
                c = stack[0][1] + 1
                if tempStr not in visited:
                    stack.append((tempStr,c))
                    visited.append(tempStr)
    stack.pop(0)
    return -1



def funct():
    f = open('A-small-attempt2.in','r')
    out = open('t2.txt','w')
    for i in range(int(f.readline())):
        print "hi",i
        stack = []
        visited = []
        line = f.readline().split(' ')
        s = line[0]
        k = int(line[1])
        stack.append((s,0))
        visited.append(s)
        flag = -1
        while flag == -1 and len(stack) > 0:
            flag = flipper(stack,k)
        if flag >= 0:
            out.write('Case #'+str(i+1)+": "+str(flag)+"\n")
        else:
            ot = "IMPOSSIBLE"
            print ot
            out.write('Case #'+str(i+1)+": "+ot+"\n")


    out.close()

if __name__ == '__main__':
    funct()
