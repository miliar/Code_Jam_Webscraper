'''
Created on 13/apr/2013

@author: valentinarho
'''

if __name__ == '__main__':
    
    nomefile = "A-large"
    
    # open file input
    input = open(nomefile+'.in','r');
    out = open(nomefile+'.out','w');
    
    result = {'O':"O won", 'X':"X won", 'draw':"Draw",'not':"Game has not completed"}
    
    # number of test case
    T = int(input.readline()); 
    
    for i in range(1,T+1): #da 1 a t

        matr = ["","","",""];
        for j in range(0,4):
            matr[j] = input.readline();
        
        #flush della riga vuota
        input.readline();
        
        #controllo righe
        res = "";
        point = False #controllo se ho incontrato un punto
        finish = False
        ri = 0
        while ri < 4 and finish == False:
            co = 0; 
            cx = 0;
            for ric in range(0,4): 
                if (matr[ri][ric] == 'T'):
                    co = co+1
                    cx = cx+1
                elif (matr[ri][ric] == 'X'): 
                    cx = cx+1
                elif(matr[ri][ric] == '.'):
                    point = True
                else:
                    co = co+1
        
            if (co == 4): 
                res  = result['O']
            elif(cx == 4):
                res = result['X']
                
            if res != "": 
                finish = True;
          
            ri = ri+1  
        
        #checkcolonne se non ho gia finito con le righe
        if (finish == False):
            ri = 0
            while ri < 4 and finish == False:
                co = 0; 
                cx = 0;
                for ric in range(0,4): 
                    if (matr[ric][ri] == 'T'):
                        co = co+1
                        cx = cx+1
                    elif (matr[ric][ri] == 'X'): 
                        cx = cx+1
                    elif(matr[ric][ri] == '.'):
                        point = True
                    else:
                        co = co+1
            
                if (co == 4): 
                    res  = result['O']
                elif(cx == 4):
                    res = result['X']
                    
                if res != "": 
                    finish = True;
              
                ri = ri+1  
        
        #checkdiagonale2
        if (finish == False):
            ri = 0
            col = 4
            co = 0
            cx = 0
            while ri < 4:
                col = col-1
                
                if (matr[ri][col] == 'T'):
                    co = co+1
                    cx = cx+1
                elif (matr[ri][col] == 'X'): 
                    cx = cx+1
                elif(matr[ri][col] == '.'):
                    point = True
                else:
                    co = co+1
                ri = ri+1  
                
            if (co == 4): 
                res  = result['O']
            elif(cx == 4):
                res = result['X']
                
            if res != "": 
                finish = True;
        
        #checkdiagonale1
        if (finish == False):
            ri = 0
            co = 0
            cx = 0
            while ri < 4:
                
                if (matr[ri][ri] == 'T'):
                    co = co+1
                    cx = cx+1
                elif (matr[ri][ri] == 'X'): 
                    cx = cx+1
                elif(matr[ri][ri] == '.'):
                    point = True
                else:
                    co = co+1
                ri = ri+1  
                
            if (co == 4): 
                res  = result['O']
            elif(cx == 4):
                res = result['X']
                
            if res != "": 
                finish = True;
                
        if (finish == True):
            out.write("Case #"+str(i)+": "+res+"\n");
        elif(point == True):
            out.write("Case #"+str(i)+": "+result['not']+"\n");
        else:
            out.write("Case #"+str(i)+": "+result['draw']+"\n");
        
    
    
    pass