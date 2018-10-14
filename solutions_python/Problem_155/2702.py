if __name__=='__main__':
    test = int(input())
    for t in range(test):
        inp = input().split()
        smax = int( inp[0] )
        peoples = inp[1]

        invited = 0
        total = 0
        
        for i in range(smax+1):
            x = int( peoples[i] )
            if total < i:
                invited = invited + (i-total)
                total = i + x
            else:
                total = total + x

        print("Case #" + str(t+1) + ": " + str(invited) )    
