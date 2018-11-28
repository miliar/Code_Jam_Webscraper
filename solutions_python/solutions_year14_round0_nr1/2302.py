infile=open("small.in")
outfile=open("small.out", "a")
def output(num, count):
    outstr="Case #"
    outstr+=str(count+1)
    outstr+=": "
    outstr+=str(num)
    outstr+="\n"
    outfile.write(outstr)
    print count
N=int(infile.readline())

def readboard():
    a=[]
    for x in xrange(4):
        a.append([int(y) for y in infile.readline().strip().split(" ")])
    return a
def case():
    choice=int(infile.readline())-1
    board=readboard()
    row1=board[choice]
    print row1
    choice=int(infile.readline())-1
    board=readboard()
    row2=board[choice]
    print row2
    found=0
    for i in row1:
        try:
            ind=row2.index(i)
            if found==0:
                found=i
            else:
                print found
                return "Bad magician!"
        except (ValueError):
            print
    if found==0:
        return "Volunteer cheated!"
    else:
        return found
for c1 in xrange(N):
    output(case(), c1)
