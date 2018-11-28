#!/usr/bin/python3

def main():
    t=int(input())
    for k in range(t):
        n=int(input())
        check(n,k)
        
            
def check(n,k):
    
    if (n<=100):
        generate(n,k)
        
            
    else:
        generate1(n,k)     
    
        
        
def generate(N,t):
    if (N==100):
        print ('case #{}: {}'.format(t+1,'99'))
    else:
        
        generaten(N,t)
    
    
    
    
        
            
           
        
        
            
def generaten(N,t):
    for n in range(N,-1,-1):
        
        k=int(n%10)
        m=int(n/10)
        l=int(m%10)
        if (k>=l):break
    print('case #{}: {}'.format(t+1,n))

def generate1(N,t):
    if (N==1000):
        print ('case #{}: {}'.format(t+1,'999'))
    else:
        
        generaten1(N,t)

def generaten1(N,t):
    for n in range(N,-1,-1):
        
        k=int(n%10)
        m=int(n/10)
        l=int(m%10)
        j=int(m/10)
        f=int(j%10)
        if (k>=l and l>=f):break
    print('case #{}: {}'.format(t+1,n))
         
        

    


        
        
        
        
    
        
   
    
    
if __name__ == "__main__": main()# your code goes here