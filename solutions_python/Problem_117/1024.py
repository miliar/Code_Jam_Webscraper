f=file("BLarge.txt")

def ReadInput(f):
    """f = file"""
    lines = f.readlines()
    cases = int(lines[0])
    count = 0
    for a in range(0,cases):
        count+=1
        rxc=(lines[count]).split()
        r=int(rxc[0])
        c=int(rxc[1])
        lawn=[]
        for b in range(0,r):
            count+=1
            nlines = map(int, lines[count].split())
            lawn.append(nlines)       
        nlist = []
        for i in lawn:
            for j in i[0:c]:
                nlist.append(int(j))
        mx = max(nlist)
        mn = min(nlist)
        AllBal=[]
        for b in range(mn,mx+1):
            spots = []
            for p in range(0,r):
                for q in range(0,c):
                    if lawn[p][q] == b:
                        spots.append([p,q])
            for s in spots:
                balance = 0
                for col in range(0,c):
                    if lawn[s[0]][col]>b:
                        balance-=1
                        break
                for row in range(0,r):
                    if lawn[row][s[1]]>b:
                        balance-=1
                        AllBal.append(balance)
                        break
                    AllBal.append(balance)
                if -2 in AllBal:
                    judgement = 'NO'                    
                elif -2 not in AllBal:
                    judgement = 'YES'
        print 'Case #'+str(a+1)+': '+str(judgement)
        
L=ReadInput(f)

