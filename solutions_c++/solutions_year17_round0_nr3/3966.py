#include <iostream>
#include<algorithm>
using namespace std;
typedef long long  ll;
typedef pair<ll,ll> pll;
#include<cstring>
#define N 20
#define fr(i,x,y) for(int i=x;i<=y;i++)
#define f1 first
#define f2 second
ll n,k;


pll f(ll a,ll b)
{
    if (b==0){pll x=make_pair(-1,-1);return x;}
    if (b==1){pll x=make_pair(a-1-(a-1)/2,(a-1)/2); return x;}


    ll a1,b1;
    a1=(a-1)/2;
    b1=(b-1)/2;
    //printf("%d %d\n",a1,b1);
    pll x1,x2;
    x1=f(a1,b1);
    x2=f(a-1-a1,b-1-b1);
    if (b1!=b-1-b1) return x2;
    if (a1!=a-1-a1) return x1;
    return x2;
//    if (x1.f2>x2.f2) return x1;
//    if (x1.f2<x2.f2) return x2;
//    if (x1.f1>x2.f1) return x1;
    return x2;
}






void doit()
{
    scanf("%d%d",&n,&k);
    pll x=f(n,k);
    printf("%lld %lld\n",x.f1,x.f2);
}






int main() {
    int cas;

    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("C-small-2-attempt1.out","w",stdout);
    scanf("%d",&cas);
    int id=0;
    while (cas--)
    {
        printf("Case #%d: ",++id);
        doit();
    }
    return 0;
}