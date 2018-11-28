#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXN 100
using namespace std;

int g[MAXN+1];
int n,p;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i,c0,c1,c2,c3,m12,m13,ans;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d",&n,&p);
        for(i=0;i<n;i++)
        {
            scanf("%d",&g[i]);
        }
        if(p==2)
        {
            c0=0;
            c1=0;
            for(i=0;i<n;i++)
            {
                if(g[i]%2==0)
                {
                    c0++;
                }
                else
                {
                    c1++;
                }
            }
            ans=0;
            ans=ans+c0;
            ans=ans+(c1+1)/2;
        }
        else if(p==3)
        {
            c0=0;
            c1=0;
            c2=0;
            for(i=0;i<n;i++)
            {
                if(g[i]%3==0)
                {
                    c0++;
                }
                else if(g[i]%3==1)
                {
                    c1++;
                }
                else
                {
                    c2++;
                }
            }
            ans=0;
            ans=ans+c0;
            m12=min(c1,c2);
            c1=c1-m12;
            c2=c2-m12;
            ans=ans+m12;
            ans=ans+(c1+2)/3;
            ans=ans+(c2+2)/3;
        }
        else
        {
            c0=0;
            c1=0;
            c2=0;
            c3=0;
            for(i=0;i<n;i++)
            {
                if(g[i]%4==0)
                {
                    c0++;
                }
                else if(g[i]%4==1)
                {
                    c1++;
                }
                else if(g[i]%4==2)
                {
                    c2++;
                }
                else
                {
                    c3++;
                }
            }
            ans=0;
            ans=ans+c0;
            m13=min(c1,c3);
            c1=c1-m13;
            c3=c3-m13;
            ans=ans+m13;
            ans=ans+c2/2;
            c2=c2%2;
            ans=ans+c1/4;
            c1=c1%4;
            ans=ans+c3/4;
            c3=c3%4;
            if((c2>=1)&&(c1>=2))
            {
                ans++;
                c2=c2-1;
                c1=c1-2;
            }
            if((c2>=1)&&(c3>=2))
            {
                ans++;
                c2=c2-1;
                c3=c3-2;
            }
            if((c2>=1)||(c1>=1)||(c3>=1))
            {
                ans++;
            }
        }
        printf("Case #%d: %d\n",c+1,ans);
    }
    return 0;
}
