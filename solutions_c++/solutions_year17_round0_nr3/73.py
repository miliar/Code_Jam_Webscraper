#include<bits/stdc++.h>
using namespace std;
using ll = long long;

map<ll,map<ll,ll>> cache;

void foo(int d, ll n, map<ll,ll> & cnt)
{
    if(d == 0)
    {
        cnt[n]++;
        return;
    }
    if(cache.find(n) != cache.end())
    {
        for(auto p : cache[n])
            cnt[p.first] += p.second;
        return;
    }
    map<ll,ll> tmp;
    if(n&1)
    {
        foo(d-1, n/2, tmp);
        for(auto p : tmp)
            tmp[p.first] += p.second;
    }
    else
    {
        foo(d-1,(n-1)/2,tmp);
        foo(d-1,n/2,tmp);
    }
    cache[n] = tmp;
    for(auto p : tmp)
        cnt[p.first] += p.second;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        cache.clear();
        printf("Case #%d: ",t);
        ll n,k,ans=-1;
        scanf("%lld%lld",&n,&k);
        for(int d = 0; d < 64; d++)
        {
            ll m = 1LL<<d;
            k -= m;
            if(k > 0) continue;
            k += m;
            map<ll,ll> cnt;
            foo(d,n,cnt);
            for(auto it = cnt.rbegin(); it != cnt.rend(); it++)
            {
                auto p = *it;
                if(p.second < k)
                {
                    k -= p.second;
                    continue;
                }
                ans = p.first;
                break;
            }
            break;
        }
        if(ans == 0) puts("0 0");
        else printf("%lld %lld\n",ans/2, (ans-1)/2);
    }
}
