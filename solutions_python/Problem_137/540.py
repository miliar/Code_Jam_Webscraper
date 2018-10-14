f = open('/Users/anna/Mine/Code_Jam_2014/c_sol', 'w')  
tasks=[]
N=0
def read_tasks():
    with open('/Users/anna/Mine/Code_Jam_2014/C-large.in','r') as f:
    #with open('/Users/anna/Mine/Code_Jam_2014/c_small','r') as f:
        global N
        N=int(f.readline())
        for line in f:
            line_lst = map(int, line.split(" "))
            tasks.append(line_lst)
        #print "N", N, type(N)

def solve(R,C,M):
    if  (R>1) and (C>1) and ((M+1)<R*C) and (M+4>(R*C)):
        print "Impossible"
        f.write("Impossible\n")
    elif R==1:
        col=[]
        for i in range(0,M):
            col.append("*")
        for i in range (0,C-M-1):
            col.append(".")
        col.append("c")
        col_to_write="".join(map(str,col))
        print col_to_write
        f.write(col_to_write + "\n")
    elif (C==1):
        for i in range(0,M):
            print "*"
            f.write("*\n")
        for i in range (0,R-M-1):
            print "."
            f.write(".\n")
        print "c"
        f.write("c\n")
    elif (M+1)==R*C:
        for i in range(0,R-1):
            for j in range(0,C):
                f.write("*")
            f.write(" \n")
        for j in range(0,C-1):
            f.write("*")
        f.write("c\n")
    elif R==2:
        if (M%2)==0:
            k_res=M/2
            for i in range(0,k_res):
                f.write("*")

            for i in range(k_res,C):
                f.write(".")
            f.write(" \n")
            for i in range(0,k_res):
                f.write("*")
     
            for i in range(k_res,C-1):
                f.write(".")
            f.write("c\n")
        else:
            f.write("Impossible\n")
    elif C==2:
        if ((M%2)==0):
            k_res=M/2
            for i in range(0,k_res):
                f.write("**\n")
            for i in range(k_res,R-1):
                f.write("..\n")
            f.write(".c\n")
        else:
            f.write("Impossible\n")
            
    else:
        if M<(C*(R-2)-1):
            mine_lines=M/C #number of lines full of mines
            res=M%C #residual of mine-lines 
            if not (res==C-1):
                for i in range(0,mine_lines):
                    for j in range(0,C):
                        f.write("*")
                    f.write(" \n")
                for i in range(0,res):
                    f.write("*")
                for i in range(res,C):
                    f.write(".")
                f.write(" \n")
                for i in range(mine_lines+1,R-1):
                    for j in range(0,C):
                        f.write(".")
                    f.write(" \n")
                for j in range(0,C-1):
                    f.write(".")
                f.write("c\n")
            else:
                for i in range(0,mine_lines):
                    for j in range(0,C):
                        f.write("*")
                    f.write(" \n")
                for i in range(0,res-1):
                    f.write("*")
                for i in range(res-1,C):
                    f.write(".")
                f.write(" \n")
                f.write("*")
                for i in range(1,C):
                    f.write(".")
                f.write(" \n")
                for i in range(mine_lines+2,R-1):
                    for j in range(0,C):
                        f.write(".")
                    f.write(" \n")
                for j in range(0,C-1):
                    f.write(".")
                f.write("c\n")
        else:
            G_rest=C*3-( M-C*(R-3))
            if (G_rest==2) or (G_rest==3) or (G_rest==5) or (G_rest==7):
               f.write("Impossible \n")
            elif G_rest==4:  
                for i in range(0,R-2):
                    for j in range(0,C):
                        f.write("*")
                    f.write(" \n")
                for i in range(0,C-2):
                    f.write("*")
                for i in range(0,2):
                    f.write(".")
                f.write(" \n")
                for i in range(0,C-2):
                    f.write("*")

                f.write(".c")
                f.write(" \n")
            else:
                k_res=G_rest%3
                if k_res==2:
                    g_3=G_rest/3
                    for i in range(0,R-3):
                        for j in range(0,C):
                            f.write("*")
                        f.write(" \n")
                    for i in range(0,C-g_3):
                        f.write("*")
                    for i in range(C-g_3,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3-1):
                        f.write("*")
                    for i in range(C-g_3-1,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3-1):
                        f.write("*")
                    for i in range(C-g_3-1,C-1):
                        f.write(".")
                    f.write("c\n")
                elif k_res==0:
                    g_3=G_rest/3
                    for i in range(0,R-3):
                        for j in range(0,C):
                            f.write("*")
                        f.write(" \n")
                    for i in range(0,C-g_3):
                        f.write("*")
                    for i in range(C-g_3,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3):
                        f.write("*")
                    for i in range(C-g_3,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3):
                        f.write("*")
                    for i in range(C-g_3,C-1):
                        f.write(".")
                    f.write("c\n")
                elif k_res==1:
                    g_3=(G_rest-4)/3
                    for i in range(0,R-3):
                        for j in range(0,C):
                            f.write("*")
                        f.write(" \n")
                    for i in range(0,C-g_3):
                        f.write("*")
                    for i in range(C-g_3,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3-2):
                        f.write("*")
                    for i in range(C-g_3-2,C):
                        f.write(".")
                    f.write(" \n")
                    for i in range(0,C-g_3-2):
                        f.write("*")
                    for i in range(C-g_3-2,C-1):
                        f.write(".")
                    f.write("c\n")

                
                
                 
            
        
            
    
    
  
read_tasks()
for i in range(0,N):
    str_print="Case #"+str(i+1)+":"
    print str_print
    f.write(str_print + "\n")
    
    R=tasks[i][0]
    C=tasks[i][1]
    M=tasks[i][2]
    print "R, C, M", R, C, M
#    f.write(str(R)+" "+str(C)+" "+str(M)+"\n")
    solve(R,C,M)
 #   f.write("\n")
