#include <stdio.h>
#include <iostream>



bool goodnum(long num);

int main()
{
    int T=0;
    int i=1;
    int j=0;
    long temp=0;
    bool rt = false;
    
    std::cin>>T;
    long N[T];
    
    while(i<=T)
    {
        std::cin>>N[i];
        i++;
    }
    
    i=1;

    while(i<=T)
    {
        temp=N[i];
        
        if (temp <10)
        {
            printf("Case #%d: %ld \n", i,temp);
        }
        else
        {
            while(temp>0)
            {
                rt=goodnum(temp);
                
                if(rt==true)
                    break;
                
                temp--;
            }
            printf("Case #%d: %ld \n", i,temp);
            
        }
        i++;
    }
    return 0;
}

bool goodnum(long num)
{
    int d=0;
    int l=9;
    
    while(num>0)
    {
        d=num%10;
        
        if(d<=l)
            l=d;
        else
            return false;
            
        num=num/10;
    }
    return true;
}