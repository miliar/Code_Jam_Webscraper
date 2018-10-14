val =[]
for i in range(0,4):
    val+=[[0]*4]
val[0][0]="1000"
val[0][1]="1100"
val[0][2]="1000"
val[0][3]="1100"

val[1][0]="1100"
val[1][1]="1100"
val[1][2]="1110"
val[1][3]="1100"

val[2][0]="1000"
val[2][1]="1110"
val[2][2]="1010"
val[2][3]="1111"

val[3][0]="1100"
val[3][1]="1100"
val[3][2]="1111"
val[3][3]="1101"
t = input()
for i in xrange(1,t+1):
    print "Case #"+str(i)+":",
    inp = raw_input().split()
    x = int(inp[0])
    r = int(inp[1])
    c = int(inp[2])
    if(val[r-1][c-1][x-1]=='1'):
        print "GABRIEL"
    else:
        print "RICHARD"
    
