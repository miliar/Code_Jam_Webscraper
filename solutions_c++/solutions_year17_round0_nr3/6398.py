#include <bits/stdc++.h>
using namespace std;
typedef long long ull;
void solve()
{
    ull n,k;
    scanf("%lld%lld",&n,&k);
    map<ull,ull> mp;
    mp[-n]=1;
    while(k)
    {
        ull l=-mp.begin()->first,r=mp.begin()->second;
        if(l==1)    break;
        if(r>=k)    break;
        k-=r;
        mp.erase(-l);
        mp[-(l/2)]+=r;
        mp[-((l-1)/2)]+=r;
    }
    ull l=-mp.begin()->first;
    printf("%lld %lld\n",l/2,(l-1)/2);
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",cas++);
        solve();
    }
}
