'''
Created on Apr 11, 2015

@author: mostasem
'''

def generate_omino_combinations(n):
    omnios_combs = {}
    omnios_combs[(1,n)] = True
    for i in range(2,n):
        for j in range(2,n):
            if(i*j >= n and omnios_combs.get((i,j)) == None  and omnios_combs.get((j,i)) == None and (i*j) / n == 1):
                omnios_combs[(i,j)] = True

    return omnios_combs.keys()

        
# The dummy way : 

def determine_winner(R,C,X):
    ominos_combs = generate_omino_combinations(X)
    #print ominos_combs
    answer = ''
    
    if(X == 1):
        answer = 'GABRIEL'
        
    elif(X == 2):
        ans = check_numeric(R,C,X)
        if(ans):
            answer = 'GABRIEL'
        else:
            answer = 'RICHARD'
            
    elif(X == 3):
        for i in range(len(ominos_combs)):
            x,y = ominos_combs[i]
            if(x == 1 or y == 1):
                ans = check_numeric(R,C,X)
                if(not ans):
                    answer = 'RICHARD'
                    break
            else:
                if(R*C < x*y):
                    answer = 'RICHARD'
                    break
                else :
                    ans = check_numeric(R,C,X)
                    if(not ans):
                        answer = 'RICHARD'
                        break
                    else:
                        answer = 'GABRIEL'
                        
    elif(X == 4):
        for i in range(len(ominos_combs)):
            x,y = ominos_combs[i]
            if(x == 1 or y == 1):
                ans = check_numeric(R,C,X)
                if(not ans):
                    answer = 'RICHARD'
                    break
                
            else:
                if(R*C < x*y):
                    answer = 'RICHARD'
                    break
                else :
                    if(R == C == 4 or ( R == 3 and C == 4) or (C == 3 and R == 4)):
                        answer = 'GABRIEL'
                    else:
                        answer = 'RICHARD'
                        
        
    return answer    
        
    
    
def check_numeric(R,C,X):
    rem = R*C % X
    answer = False
    if(rem == 0):
        answer = True
    else:
        answer = False
    return answer



f_r = open('D-small-attempt1.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("D.out", "w")
result = ""
for i in range(n_test):
    X,R,C = map(int,f_r.readline().split())
    result = determine_winner(R,C,X)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()