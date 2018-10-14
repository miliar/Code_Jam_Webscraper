'''
Created on Apr 14, 2012

@author: Ankit
'''
file_out = open('out.txt',"w")
out = ''
idx=0
with open('B-large.in',"r") as file_inp:
    T = int(file_inp.readline())
    for l in file_inp:
        inp = l.split()
        N = int(inp[0])
        S = int(inp[1])
        p = int(inp[2])
        count = 0
        idx=idx+1
        for i in range(N):
            ti = int(inp[3+i])
            if ti and p:
                if ti%3 == 0:            
                    mx = ti/3
                    if mx >= p:
                        count = count + 1
                        #print "ti:",ti
                    elif p-mx==1 and S!=0:
                        count = count + 1
                        S = S-1
                        #print "ti:",ti, "S:", S
                elif ti%3 == 2:
                    mx = (ti+1)/3
                    if mx >= p:
                        count = count + 1
                        #print "ti:",ti
                    elif p-mx==1 and S!= 0:
                        count = count + 1
                        S = S-1
                        #print "ti:",ti, "S:", S
                elif ti%3 == 1:
                    mx = (ti+2)/3
                    if mx >= p:
                        count = count + 1
                        #print "ti:",ti
            elif p==0:
                count = N
        out = out+"Case #"+str(idx)+": "+str(count)
        file_out.write(out)
        out = "\n"
        
file_out.close()