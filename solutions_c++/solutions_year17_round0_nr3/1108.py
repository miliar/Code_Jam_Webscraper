#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

typedef long long LL;
int T;
int kase=0;
LL n,k;

inline void proc(LL n)
{
//    printf("%lld %lld\n",(n+1)>>1,(n-1))
    if(n&1)
        printf("%lld %lld\n",(n-1)>>1,(n-1)>>1);
    else
        printf("%lld %lld\n",n>>1,(n-1)>>1);
}
inline void case_init()
{
    scanf("%lld%lld",&n,&k);
    printf("Case #%d: ",++kase);
}
inline void case_solve()
{
    int dep=0;
    LL a,b,na,nb;
    while(k>(1ll<<dep))
    {
        k-=(1ll<<dep);
        ++dep;
    }
    for(int i=0;i<dep;++i) n-=(1ll<<i);
    a=n/(1ll<<dep);
    b=a+1;
    nb=n-(a*(1ll<<dep));
    na=(1ll<<dep)-nb;
    if(k<=nb) proc(b);
    else proc(a);
    return ;
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    for(scanf("%d",&T);T;--T)
    {
        case_init();
        case_solve();
    }
    return 0;
}
