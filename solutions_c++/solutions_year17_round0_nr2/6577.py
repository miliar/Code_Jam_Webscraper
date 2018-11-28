#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
using namespace std;
const int maxn=20;
int test,a[maxn],mi[maxn],n;
long long x,res,xx;


bool check(long long x)
{
    n=0;
    while (x)
    {
        a[++n]=x%10;
        x/=10;
    }
    for (int i=n;i>=2;--i)
        if (a[i]>a[i-1]) return false;
    return true;
}

long long vet(long long x)
{
    for (int i=x;i>=1;--i)
    {
        if (check(i)) return i;
    }
}


bool kt(int u,int x)
{
    for (int i=u;i<=n;++i)
    {
        if (x<a[i]) return true;
        if (x>a[i]) return false;
    }
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&test);
    for (int t=1;t<=test;++t)
    {
        res=n=0;
        scanf("%lld",&x);
        xx=x;
        while (x)
        {
            a[++n]=x%10;
            x/=10;
        }
        reverse(a+1,a+n+1);
        mi[n]=a[n];
        for (int i=n-1;i>=1;--i)
            mi[i]=min(mi[i+1],a[i]);
        bool small=false;
        {
            for (int i=1;i<=n;++i)
            {
                if (small) res=res*10+9;
                else
                {
                    if (i==n || kt(i+1,a[i])) res=res*10+a[i];
                    else
                    {
                        res=res*10+a[i]-1;
                        small=true;
                    }
                }
            }
        }
//        {
//            printf("Case #%d: %lld %lld\n",t,res,vet(xx));
//            if (res!=vet(xx))
//            {
//                cout<<xx;
//                return 0;
//            }
//        }
        printf("Case #%d: %lld\n",t,res);
    }
    return 0;
}
