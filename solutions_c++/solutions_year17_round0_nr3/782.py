#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef long long ll;

map<ll,ll,greater<ll>> m;

int main()
{
    freopen("/Users/qianjay/Documents/cc/in", "r", stdin);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        printf("Case #%d: ",test);
        ll n,k;
        scanf("%lld%lld",&n,&k);
        m.clear();
        m[n]=1;
        ll res=0;
    
        while(k>0)
        {
            if(k<=m.begin()->second)
            {
                res=m.begin()->first;
                break;
            }
            else
            {
                k-=m.begin()->second;
                ll val=m.begin()->first;
                m[(val-1)/2]+=m[val];
                m[val-1-(val-1)/2]+=m[val];
                m.erase(val);
            }
        }
        ll a=(res-1)/2,b=res-1-(res-1)/2;
        printf("%lld %lld\n",max(a,b),min(a,b));
    }
    return 0;
}
