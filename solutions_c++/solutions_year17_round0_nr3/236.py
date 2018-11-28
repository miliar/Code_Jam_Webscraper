#include <cstdio>
#include <map>

using namespace std;

typedef long long lld;
map<lld,lld> d;
lld mid;

lld solve(lld n)
{
    if(n<mid) return 0;
    if(d.count(n)) return d[n];
    if(n&1) d[n]=1+2*solve(n/2);
    else d[n]=1+solve(n/2-1)+solve(n/2);
    return d[n];
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        lld n,k;
        scanf("%lld%lld",&n,&k);
        lld st=1,dr=n;
        while(st<=dr)
        {
            d.clear();
            mid=(st+dr)/2;
            lld nr=solve(n);
            if(nr>=k) st=mid+1;
            else dr=mid-1;
        }
        long long a,b;
        if(dr==1) a=b=0;
        else if(dr&1) a=b=dr/2;
        else a=dr/2, b=dr/2-1;
        printf("Case #%d: %lld %lld\n",t,a,b);
    }
    return 0;
}
