#include<bits/stdc++.h>
using namespace std;
bool tidy(long long n)
{
    long long a,p,q,r,s,t,u;
    a=1;
    p=n%10;
    q=n/10;
    while(q>0)
    {
        r=q%10;
        if(p>=r)
        {
            p=r;
            q=q/10;
        }
        else
            return false;
    }
    if(a==1)
        return true;
}
int main()
{
    long long i,j,k,l,m,n,p,o;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
     scanf("%lld",&n);
     for(k=1;k<=n;k++)
     {
         scanf("%lld",&m);
         for(i=m;i>=1;i--)
         {
             if(tidy(i))
             {
                 printf("Case #%lld: %lld\n",k,i);
                 break;
             }
         }
     }
     return 0;
}
