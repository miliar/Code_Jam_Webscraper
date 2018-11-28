#problemB


def toList(n):
    if n == 0:
        return [0]
    li = []
    while n!= 0:
        li.append(n%10)
        n//=10
    li.reverse()
    return li

def toInt(l):
    n = 0
    for i in l:
        n *=10
        n+=i
    return n


def figure(n):
    l = toList(n)
    buffer = []
    for i in range(len(l)-1):
        
        if l[i] < l[i+1]:
            # it doesn't have to change
            buffer = []
            continue
        elif l[i] > l[i+1]:
            start = i
            if buffer == []:
                l[i] -=1
            else:
                l[buffer[0]] -=1
                start = buffer[0]
            for ii in range(start+1,len(l)):
                l[ii] = 9
            break
        elif l[i] == l[i+1]:
            buffer.append(i)
    return toInt(l)
        

def problem2(fileName):
    f = open(fileName,'r')
    testNum = int( f.readline())


    output = open("Output.txt",'w')
    
    for i in range(testNum):
        s = f.readline().strip()
        n = int(s)
        output.write("Case #"+ str(i+1) +": "+str(figure(n)))
        output.write("\n")
        
if __name__ == '__main__':
    problem2("B-large.in.txt")
    print("Complete")
