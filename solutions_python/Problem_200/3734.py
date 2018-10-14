def g(x):
    a = 10
    counter = 0
    while x >= 1 and counter < 4:
        b = x % 10
        if b > a:
            return False
        a = b % 10
        x = x / 10
        # print x, a, b
        counter += 1
    return True

def f(x):
    t = x
    b = True
    counter = 0
    while t > 0 and counter < 200:
        if g(t):
            break
        t -= 1
        counter += 1
    return t
file = open('C:\\Users\\V\\Downloads\\B-small-attempt0.in','r')
b = file.read()
file.close()    
data = b.split('\n')
n = int(data[0])
file = open('C:\\Users\\V\\Downloads\\Codejam.txt','w')
for i in range(n):
    t = int(data[i + 1])
    a = f(t)
    file.write("Case #" + str((i + 1)) + ": "  + str(a) + '\n')
file.close()