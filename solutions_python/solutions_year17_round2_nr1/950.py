
t = int(input());
maxi = 0;

for i in range(t):
    x = input().split();
    d = int(x[0]);
    n = int(x[1]);
    for y in range(n):
        horse = input().split();
        horseP = int(horse[0]);
        horseS = int(horse[1]);
        horseD = int(d)-int(horseP);
        horseT = horseD/horseS
        if( horseT>maxi):
            maxi = horseT;
       
    print("Case #"+str(i+1)+": "+str(int(d)/maxi));
    maxi=0;    
                
                
        
