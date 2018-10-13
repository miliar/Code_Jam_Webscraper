

def process(line,count):
    maxShy = line[0]
    newline = line[2:]
    standing = 0
    extra = 0

    for i in range(0,int(maxShy)+1):
        #print "count", i
        if(standing >= i):
            standing += int(newline[i])
            #print "add standing", int(newline[i])
        else:
            #print "add extra", int(newline[i])
            if (int(newline[i]) > 0):
                extra += i-standing
                standing += extra
                standing += int(newline[i])

    str1 = "Case #"+str(count)+": "+ str(extra)+"\n"
    out.write( str1)
        
count = 1

out = open('output', 'a')
f = open('standingOinput', 'r')

tasks = int(f.readline())

for i in range(0,tasks):
    
    process(f.readline(),count)
    count+=1

