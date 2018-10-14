
n = int(input());

for i in range(n):
    count=0;
    seq,k =input().split();
    k = int(k);
    seq = list(seq);
    length = len(seq);
    for q in range(length):
        if seq[q]=='+':
            continue;
            
        else:
            if(q+k)>length:
                break;
            for j in range(k):
                if seq[q+j]=="+":
                    seq[q+j]="-";
                else:
                    seq[q+j]="+"
            count = count+1;
    if "-" in seq:
        print("Case #"+str(i+1)+": "+"IMPOSSIBLE");
    else:
        print("Case #"+str(i+1)+": "+str(count));
        
                
                
        
