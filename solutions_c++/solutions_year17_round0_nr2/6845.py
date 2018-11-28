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
    ll t,i,j,k,m,z,ans,a,n,b,l;
    scanf("%lld",&t);
    //printf("t=%d ",t);
    for(z=1;z<=t;z++)
    {
        scanf("%lld",&n);
        j=n;
        m=0;
        l=0;
        while(n!=0)
        {
            a=n%10;
            l=l*10+a;
            n/=10;
            m++;
        }
        
        //printf("l=%lld m=%lld @@@",l,m);
        a=l%10;
        l/=10;
        n=a;
        k=1;
        while(l!=0)
        {
            b=l%10;
            if(b<a)
              break;
            else
              n=n*10+b;
              
            a=b;  
            k++;
            l/=10;
        }
        if(k==m)  
          printf("Case #%lld: %lld\n",z,j);
        else
        {
        //printf("n=%lld ",n);
        a=n%10;
        n/=10;
        l=a;
        b=n%10;
        n/=10;
        while(b>a-1)
       {
           
           a=b;
           b=n%10;
           n/=10;
           m++;
       }
       
       //printf("k=%lld m=%lld",k,m);
        
        n=n*100+b*10+a-1;
        k=m-k;
        while(k--)
        {
            n=n*10+9;
        }
        
        if(m==1)
          printf("Case #%lld: %lld\n",z,a);
        else
          printf("Case #%lld: %lld\n",z,n);
          }
        
          
    }
	
	return 0;
}

