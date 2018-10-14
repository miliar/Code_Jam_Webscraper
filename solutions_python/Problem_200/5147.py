#Tidy numbers

t=int(input())

for j in range(t):
    tal=int(input())
    tall=tal
    for i in range(0, tal):
        sak=0
        x=0
        for b in str(tall):
            if int(b)>=sak:
                sak=int(b)
            else:
                x=1
                break
        if x==0:
            print("Case #" + str(j+1) + ": " + str(tall))
            break
        tall=tall-1
