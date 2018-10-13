myinf = "sample.txt"
myinf = "C-small-attempt2.in"
#myinf = "B-large-practice.in"

#myout = open("output.txt",'wt')
myout = open("output1.txt",'wt')
#myout = open("output2.txt",'wt')

#table = [[1,i,j,k],[i,-1,k,-j],[j,-k,-1,i],[k,j,-i,-1]]
table = [[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]
table_inv = [[1,-2,-3,-4],[2,1,-4,3],[3,4,1,-2],[4,-3,2,1]]
conv = {'i':2,'j':3,'k':4}
conv2 = {1:'1',2:'i',3:'j',4:'k'}

myin = open(myinf,'rt').read().split('\n')
num_case = int(myin[0])
print(num_case)
for i in range(num_case):
    shift=i*2+1   
    nums= myin[shift].split()
    L=int(nums[0])
    X=int(nums[1])
    line = myin[shift+1]
    total_len = L*X
    print(i,L,X)
    written=False
    
    #special case handling
    if total_len<=2:            
        myout.write("Case #%d: %s\n"%((i+1),"NO"))
    elif total_len==3:
        if line=="ijk":
            myout.write("Case #%d: %s\n"%((i+1),"YES"))
        else:
            myout.write("Case #%d: %s\n"%((i+1),"NO"))
    #general case
    else:

        #calculate total
        c=1
        for j in range(total_len):
            if c<0:
                c=-table[-c-1][conv[line[j%L]]-1]
            else:
                c=table[c-1][conv[line[j%L]]-1]  
        print('c',c)
        if c!=-1:
            print("NO")
            myout.write("Case #%d: %s\n"%((i+1),"NO"))
        else:


            k=X
            j=0
            index_i=0                

            while index_i<total_len:
                if index_i:
                    c=table[conv['i']-1][conv[line[index_i%L]]-1]
                else:
                    c=conv[line[0]]
                while c!=conv['i'] and (index_i<total_len):
                    index_i+=1
                    if c<0:
                        c=-table[-c-1][conv[line[index_i%L]]-1]
                    else:
                        c=table[c-1][conv[line[index_i%L]]-1]   
                index_i+=1
                
                if c!=conv['i']:
                    break

                c=conv[line[index_i%L]]
                index_j=index_i
                while c!=conv['j'] and (index_j<total_len):
                    index_j+=1
                    if c<0:
                        c=-table[-c-1][conv[line[index_j%L]]-1]
                    else:
                        c=table[c-1][conv[line[index_j%L]]-1]
                
                if c==conv['j']:
                    written=True
                    myout.write("Case #%d: %s\n"%((i+1),"YES"))
                    break


            if not written:
                print("false")
                myout.write("Case #%d: %s\n"%((i+1),"NO")) 

        '''

        while index_i<total_len:

            while ci!=conv['i'] and (index_i<total_len):
                index_i+=1
                if ci<0:
                    ci=-table[-ci-1][conv[line[index_i%L]]-1]
                else:
                    ci=table[ci-1][conv[line[index_i%L]]-1]                
                #print('i', index_i,ci,conv2[abs(ci)])
            index_i+=1
            if ci<0:
                ci=-table[-ci-1][conv[line[index_i%L]]-1]
            else:
                ci=table[ci-1][conv[line[index_i%L]]-1]


            cj=conv[line[index_i%L]]
            index_j=index_i
            while index_j<total_len:            
                while cj!=conv['j'] and (index_j<total_len): 
                    if cj<0:
                        cj=-table[-cj-1][conv[line[index_j%L]]-1]
                    else:
                        cj=table[cj-1][conv[line[index_j%L]]-1]               
                    index_j+=1                
                    #print('j ',index_j,cj,conv2[abs(cj)])   

                index_j+=1
                if cj<0:
                    cj=-table[-cj-1][conv[line[index_j%L]]-1]
                else:
                    cj=table[cj-1][conv[line[index_j%L]]-1]
                
                ck=conv[line[index_j%L]]     
                for index_k in range(index_j,total_len):
                    #print('ik  ', index_k)
                    if ck<0:
                        ck=-table[-ck-1][conv[line[index_k%L]]-1]
                    else:
                        ck=table[ck-1][conv[line[index_k%L]]-1]
                    #print('k ',ck,conv2[abs(ck)])   

                if ck==conv['k']:
                    myout.write("Case #%d: %s\n"%((i+1),"YES"))
                    print("true")
                    written=True
                    break

        if not written:
            print("false")
            myout.write("Case #%d: %s\n"%((i+1),"NO"))   
        #myout.write("Case #%d: %s\n"%((i+1),"TRY"))
        '''

myout.close()    
