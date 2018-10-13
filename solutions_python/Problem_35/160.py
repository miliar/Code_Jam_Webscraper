
def mark(sink, st, a, label, flow, topleft, H, W):
    i = sink[0]
    j = sink[1]
    
    label[i][j] = st
    (m,n)=topleft[st]
    if(i<m or (i==m and j<n)):
        topleft[st] = (i,j)

    if(i != 0 and flow[i-1][j]=="s" and label[i-1][j] != st):
        mark((i-1,j), st, a, label, flow, topleft, H, W)
    if(i != H-1 and flow[i+1][j] == "n" and label[i+1][j] != st):
        mark((i+1,j), st, a, label, flow, topleft, H, W)
    if(j != 0 and flow[i][j-1] == "e" and label[i][j-1]!=st):
        mark((i,j-1), st, a, label, flow, topleft, H, W)
    if(j != W-1 and flow[i][j+1] == "w" and label[i][j+1]!=st):
        mark((i,j+1), st, a, label, flow, topleft, H, W)
    
      

def solve(a,H,W,casenumber): 
          
     sinks = []
     flow = []
     label = []
     topleft = {}

     for i in range(H):
         row = range(W)
         flow.append(row)
         label.append(row)

     for i in range(H):
         for j in range(W):        
             c = a[i][j]
             
             if (i!=H-1 and a[i+1][j]<= c):
                 flow[i][j] = "s"
                 c = a[i+1][j]
             
             if (j!=W-1 and a[i][j+1]<= c):
                 flow[i][j] = "e"
                 c = a[i][j+1]
             
             if (j!=0 and a[i][j-1]<= c ):
                 flow[i][j] = "w"
                 c = a[i][j-1]
             
             if (i!=0 and a[i-1][j]<= c ):
                 flow[i][j] = "n"
             
             if (i == 0 or a[i-1][j]>=a[i][j]) and (i == H-1 or a[i+1][j]>=a[i][j]) and (j == 0 or a[i][j-1]>=a[i][j]) and (j == W-1 or a[i][j+1]>=a[i][j]):
                 sinks.append((i,j))
                 flow[i][j] = 0
                 
            
     for i in range(len(sinks)):
        topleft[str(i)]=(H-1,W-1)
        
     for i in range(len(sinks)):
         mark(sinks[i],str(i),a,label, flow, topleft, H, W) 
    
     reverse = {}
     for k, v in topleft.iteritems():
         tmp1 = str(v[0]).zfill(3)         
         tmp2 = str(v[1]).zfill(3)
         reverse[tmp1+tmp2]= k
     
     new = {}
     i = 97
     
     tmp = reverse.keys()
     tmp.sort()
     
     for k in tmp:
         new[reverse[k]]= chr(i)
         i = i+1
      
     for i in range(H):
         for j in range(W):
             label[i][j] = new[label[i][j]]
     
     return label
     
             
def main():
    f = open("./Desktop/B-large.in")
    g = open("./Desktop/output2","w")
    numcases = int(f.readline())
    
    for i in range(numcases):
        tmp = f.readline()
        t = tmp.partition(" ")
        H = int(t[0])
        W = int(t[2])
        
        matrix = []
        for j in range(H):
            tmp = f.readline()
            row = []
            for k in range(W-1):
                t = tmp.partition(" ")
                row.append(int(t[0]))
                tmp = t[2]
            row.append(int(tmp))
            
            matrix.append(row)
                
        label = solve(matrix,H,W,i+1)
        
        st = "Case #" + str(i+1) + ":\n"
        for i in range(H):
            for j in range(W-1):
                st = st + label[i][j] + " "
            st = st + label[i][W-1] + "\n"
        
        g.write(st)
     
        
