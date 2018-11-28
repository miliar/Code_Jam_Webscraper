

def process(dline,count):

    dArr = dline.split()
    x = int(dArr[0])
    r = int(dArr[1])
    c = int(dArr[2])
            
    gab = "GABRIEL"
    rich = "RICHARD"
    winner = gab

    if ( x >= 7):
        winner = rich
    elif ((r*c)%x != 0):
        winner = rich
    elif (x-1 > r or x-1 > c):
        winner = rich
    else:
        winner = gab

    str1 = "Case #"+str(count)+": "+ winner+"\n"
    out.write(str1)
count = 1

out = open('output', 'w')
f = open('standingOinput', 'r')

tasks = int(f.readline())

for i in range(0,tasks):
    
    process(f.readline(), count)
    count+=1

