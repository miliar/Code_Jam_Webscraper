//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;


//4-side
//int xx[] = {0,0,-1,1};
//int yy[] = {-1,1,0,0};
//6-side hexagonal
//int xx[] = {2,-2,1,1,-1,-1};
//int yy[] = {0,0,1,-1,1,-1};

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 100005
#define inf 100000000

const ll mod = 1000000007ll;

map<ll,ll> mp;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out.txt", "w", stdout);
    int te, ti;
    scanf("%d", &ti);
    for(te = 1; te <= ti; te++) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        ll ans = -1;
        mp.clear();
        mp[n] = 1;
        priority_queue<ll> qu;
        qu.push(n);
        while(!qu.empty()) {

            ll x = qu.top();
            qu.pop();
            ll cnt = mp[x];
            mp[x] = 0;
            //printf("%lld %lld\n", x, cnt);
            if(cnt>=k) {
                ans = x;
                break;
            }
            k -= cnt;
            ll a = x/2;
            ll b = (x-1)/2;
            if(mp.find(a) == mp.end()) {
                qu.push(a);
                mp[a] = 0;
            }
            mp[a] += cnt;
            if(b == 0) continue;
            if(mp.find(b) == mp.end()) {
                qu.push(b);
                mp[b] = 0;
            }
            mp[b] += cnt;
        }
        printf("Case #%d: %lld %lld\n", te, ans/2, (ans-1)/2);
    }
    return 0;
}

