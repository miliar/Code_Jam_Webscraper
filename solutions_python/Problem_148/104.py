#f = open('A-small-attempt0.in', 'r')
f = open('A-large.in', 'r')
#f = open('A-sample.in', 'r')
outpu=open('output.txt','w')
cases = int(f.readline())
for case in range(cases):
    [N,X]=[int(x) for x  in f.readline().split(" ")]
    S=[int(x) for x in f.readline().split(" ")]
    S.sort()
    count =0
    [fi,l] = [0,N-1]
    while fi<=l:
        if S[fi]+S[l]<=X:
            fi=fi+1
        l=l-1
        count =count +1
    result = str(count)
    print('Case #'+ str(case+1)+": "+ result)
    outpu.write('Case #'+ str(case+1)+": "+ result+"\n")
f.close()
outpu.close()
