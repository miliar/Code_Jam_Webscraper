n=input()
for case in range(n):
    data = [(int(i),j) for j,i in zip(*[iter(raw_input().split()[1:])]*2)]
    data += [(0, 'B'),(0, 'O')]
    res=0
    o=b=0
    O=B=1
    while data[o][1] != 'O':o+=1 
    while data[b][1] != 'B':b+=1
    On = data[o][0]
    Bn = data[b][0]
    while On or Bn:
        res+=1
        canpush = True
        if On:
            if On > O:O+=1
            elif On < O:O-=1
            elif o<b:
                canpush = False
                o+=1
                while data[o][1] != 'O':o+=1 
                On = data[o][0]
        if Bn:
            if Bn > B:B+=1
            elif Bn < B:B-=1
            elif b<o and canpush:
                b+=1
                while data[b][1] != 'B':b+=1 
                Bn = data[b][0]
       

    print "Case #%s:"%(case+1), res

