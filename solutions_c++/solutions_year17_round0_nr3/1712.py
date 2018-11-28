#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

map <ll, ll> mapper;

int main ()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d", &tc);
    for(int test=1;test <= tc ;test++)
    {
        printf("Case #%d:", test);
        ll n, k;
        scanf("%I64d %I64d", &n, &k);

        mapper[n] = 1;
        for(auto it = mapper.rbegin() ; it != mapper.rend();it++){
            ll cur = it->first;
            if(cur == 0)
                break;
            ll a = cur/2;
            ll b = cur/2 - (cur%2 == 0);
            mapper[a] += mapper[cur];
            mapper[b] += mapper[cur];
        }
        ll r = 1, cnt = 0;
        for(auto it = mapper.rbegin() ; it != mapper.rend();it++){
            ll cur = it->first;
            cnt += it->second;
            if(cnt >= k){
                r = cur;
                break;
            }
        }
        printf(" %I64d %I64d\n", r/2, r/2 - (r%2 == 0));

        mapper.clear();
    }

    return 0;
}
