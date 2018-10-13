# TODO: strip split


#f = open('B.in', 'r')
f = open('B-large.in', 'r')
g = open('outputfile.out', 'w')

T= int(f.readline())

myoutput = []

def processInput(mydigits):
    i=len(mydigits)-1
    while i>0:
        if mydigits[i]<=mydigits[i-1]:
            i -= 1
        else:
            mydigits[i] -= 1
            for j in range (i):
                mydigits[j]=9
            if i<(len(mydigits)-1):
                i +=1
            else:
                break
    return mydigits

for i in range(1,T+1):
    #pancakes, flipper = f.readline().strip().split(' ')
    N = int(f.readline())
    if N<10:
        myoutput.append(N)
        continue
    #digits
    mydigits = []
    temp = N
    while temp!=0:
        mydigits.append(temp%10)
        temp = temp//10

    temp = processInput(mydigits)
    outputstring = ''
    j=len(mydigits)-1
    while mydigits[j]==0:
        j-=1

    while j>-1:
        outputstring += str(mydigits[j])
        j -= 1

    myoutput.append(outputstring)


for i in range(1,T+1):
    g.write("Case #{}: {}\n".format(i, myoutput[i-1]))

f.close()
g.close()