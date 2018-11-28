T=int(input())
for t in range(1,T+1):
    cards1=set()
    cards2=set()
    inter=set()
    r=int(input())
    for l in range(1,4+1):
        raw=raw_input()
        if l==r:
            cards1=set(raw.split())
            
    r=int(input())
    for l in range(1,4+1):
        raw=raw_input()
        if l==r:
            cards2=set(raw.split())
            
    inter = cards1 & cards2
    if len(inter) == 0:
        print("Case #"+str(t)+": Volunteer cheated!")
    elif len(inter) > 1:
        print("Case #"+str(t)+": Bad magician!")
    else:
        print("Case #" +str(t)+ ": " + inter.pop())
    