#include <stdio.h>
#include <iostream>

using namespace std;

int count(char pancake[])
{
    int cnt = 0;
    for(int i=0;pancake[i];i++) 
     if(pancake[i] == '-') 
     cnt++;
    return cnt;
}

int main()
{
 
    int T;
   scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        int cnt=0,stringlen,len;
        char pancake[1001];
        
        scanf("%s %d",pancake,&stringlen);
        for(len=0;pancake[len];len++);
        
        for(int j=0;j<=len-stringlen+1;j++)
        {
            if(count(pancake) == 0) break;
            if(pancake[j] == '-')
            {
                cnt++;
                for(int k=0;k<stringlen;k++)
                {
                    if(pancake[j+k] == '-') pancake[j+k] = '+';
                    else pancake[j+k] = '-';
                }
            }
        }
        
        if(count(pancake) != 0) printf("Case #%d: IMPOSSIBLE\n",i);
        else 
            printf("Case #%d: %d\n",i,cnt);
    }
}