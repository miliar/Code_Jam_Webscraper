#include <stdio.h>
#include <iostream>
#include <string.h>


int main()
{
    int T=0;
    
    std::cin>>T;
    
    int K; 
    char cake[1000]="";
    
    int len=0;
    int i=1;
    int rt[T+1];
    
    while(i<=T)
    {
        scanf("%s",cake);
        std::cin>>K;
        
        len=strlen(cake);
        
        int count=0;
        int j=0;
        int p=0;
    
        for(j=0;j<strlen(cake);j++)
        {
         if(cake[j]=='-')
            {
                if(len-1-j>=K-1)
                {
                    count++;
                    p=j;
                    
                    for(;p<=j+(K-1);p++)
                    {
                        if(cake[p]=='+')
                            cake[p]='-';
                        else
                            cake[p]='+';
                    }
                }
                else
                {
                    count = 7777;
                    break;
                }
            }
        }
        
        if(count==7777)
            rt[i] = 7777;
        else
            rt[i] = count;
        
        i++;
    }
    
    i=1;
    
    while(i<=T)
    {
        if(rt[i]==7777)
        {
            printf("Case #%d: IMPOSSIBLE\n",i);
        }
        else
            printf("Case #%d: %d\n",i,rt[i]);
        i++;
    }
    
    return 0;
}