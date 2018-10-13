

t = int(input());
mini = [];
maxi = [];
index=0;
minmax = [];

def bathroomcalc():
    for j in range(n):
        if bathroom[j+1]==".":
            ls = ((j+1))-abs(bathroom.rfind("0",0,j+1))-1;
            rs = (bathroom.find("0",j+1,n+2)-((j+1)))-1;
            minmax.append([ls,rs]);
            if ls == -1:
                ls=0;
            if rs == -1:
                rs=0;

            mini.append(min(ls,rs));
            maxi.append(max(ls,rs));
        else:
            mini.append(min(0,0));
            maxi.append(max(0,0));



for i in range(t):
    n,k = map(int,input().split());
    mini=[];
    maxi=[];
    bathroom = "0"+"."*n+"0";
    #bathroom = "0..0..0"
    bathroomcalc();

    for l in range(k):
        index = 0;
        ls = mini[0];
        for j in range(n-1):
            if ls<mini[j+1]:
                index = j+1;
                ls = mini[j+1];
            elif ls==mini[j+1]:    
                if maxi[index]<maxi[j+1]:
                    index = j+1;
        bathroom = bathroom[0:index+1]+"0"+bathroom[index+1+1:];
        if(l<(k-1)):
            mini=[];
            maxi=[];
            bathroomcalc();
    print("Case #"+str(i+1)+": "+str(maxi[index])+" "+str(mini[index]));
