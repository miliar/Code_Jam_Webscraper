#include <stdio.h>
#include <math.h>
#include<cstring>
#include<vector>
#include<algorithm>
#include <iostream>
#define ll long long int 
using namespace std;

int b[1005];
char a[1005];

int main() 
{
	freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t,i,j,k,m,z,ans,o,f;
    scanf("%d",&t);
    //printf("t=%d ",t);
    for(z=1;z<=t;z++)
    {
        scanf("%s%d",a,&k);
        //printf("a=%s k=%d",a,k);
        //printf("bbbbbbbbbbbbbbbbbbb");
        m=ans=f=0;
        
        for(i=0;a[i]!='\0';i++)
        {
            b[i]=0;
            
            if(i-k<0)
              o=0;
            else
              o=b[i-k];
            
            f-=o;
            if(a[i]=='-')
            {
                if((1+f)%2)
                {
                    m=1;
                    f++;
                    b[i]=1;
                    ans++;
                }
                else
                {
                    m++;
                }
                
            }
            
            else
            {
                if((f)%2)
                {
                    m=1;
                    b[i]=1;
                    ans++;
                    f++;
                }
                else
                {
                    m++;
                }
                
            }
            
            //printf("m=%d i=%d o=%d\n",m,i,o);
        }
        
        if(m>=k || (m==i))
          printf("Case #%d: %d\n",z,ans);
        else
          printf("Case #%d: IMPOSSIBLE\n",z);
          
    }
	
	return 0;
}

