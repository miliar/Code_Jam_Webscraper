#Google code jam I/O file template

f= open('B-small-attempt3.in','r')
fout = open('B-small-attempt3-result.txt','w')

#f= open('A-large-practice.in','r')
#fout = open('A-large-result.txt','w')

#f=open('test.txt','r')
#fout = open('testresult.txt','w')

casenum = int(f.readline())

for i in range(casenum):
    num = int(f.readline())
    if num < 10:
        tidy_num = num
    elif num < 100:
        a = num // 10
        b = num % 10
        if a <= b:
            tidy_num = num
        else:
            tidy_num = (a-1)*10+9
            
    elif num < 1000:
        a = num // 100
        b = (num % 100) // 10
        c = num - a*100 - b*10
        
        if a < b:
            if b <= c:
                tidy_num = num
            else:
                temp_tidy_num = (b-1)*10+9
                tidy_num = a*100 + temp_tidy_num
                
        elif a == b:
            if b>c:
                tidy_num = (a-1)*100+99
                
            else:
                tidy_num = num        
        else:
            tidy_num = (a-1)*100+99
            
    else: 
        tidy_num = 999
    
    output = 'Case #' + str(i+1)+': '+str(tidy_num)
    fout.write(output)
    fout.write('\n')
  

fout.close()
