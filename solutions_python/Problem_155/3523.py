num = 1

f = open('main.txt')
lines=f.readlines()
for z in range(1,101):
    inp = lines[z]
    b = int(inp[0])
    x = 0
    Sum = 0
    for a in range(2,b+3):
        if Sum < a-2:
            x+=1
            Sum += 1
        Sum += int(inp[a])
    print ("Case #"+str(num)+":",x)
    num += 1
    
