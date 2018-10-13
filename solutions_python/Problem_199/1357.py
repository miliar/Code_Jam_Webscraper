#file = open("test.txt","w+")


def flip_cakes(panckaes, k,i):
    j=i; l=i;
    for j in range( i, i+k):
        if(panckaes[j]=='+'):
            panckaes[j] = '-'
        else:
            panckaes[j] = '+'
        j+=1
    return l

def is_impossible(panckaes, k):
    for l in range(1,k+1):
        if( panckaes[-l]=='-'):
            return True
    return False



rfile = open("A-large.in.txt","r")
wfile =  open("A-large_out.txt","w+")
T = int (rfile.readline()[:-1])
case_no=0
for line in rfile:
    case_no+=1
    if(line[-1]=='\n'):
        lineSplit=line[:-1].split(' ')
    else:
        lineSplit = line.split(' ')
    print lineSplit
    panckaes = list(lineSplit[0])
    k = int(lineSplit[1])
    i=0; flips=0;
    while i <= len(panckaes)-k:

        if (panckaes[i]=='-'):
            flips+=1
            flip_cakes(panckaes, k, i)
            #print panckaes
        i+=1

    if is_impossible(panckaes,k):
        wfile.write('Case #%d: IMPOSSIBLE\n'%case_no)
    else:
        wfile.write('Case #'+str(case_no)+': '+str(flips)+'\n' )
    print flips

rfile.close()
wfile.close()

