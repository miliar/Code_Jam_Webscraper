file = open("input.txt","r");
case = 0;
for _ in range(int(file.readline().strip())) :
    case+=1;
    num = file.readline().strip()
    #print(sorted(num));
    if num == ''.join(sorted(num)) :
        print("Case #",case,": ",num,sep = "");
        continue;
    while int(num)>0 :
        num = str(int(num)-1)
        if num == ''.join(sorted(num)) :
            print("Case #",case,": ",num,sep = "");
            break;
    
