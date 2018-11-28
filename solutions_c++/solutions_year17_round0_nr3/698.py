#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype> 
#include <ctime>
#include <cmath>
// #include <tuple> // c++11
using namespace std;

#define st first
#define nd second
#define sz(col) ((int) col.size())
#define MEM(a,b) memset(a,b,sizeof(a))
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=a;i<=(b);++i)
#define getmid(l,r) ((l) + ((r) - (l)) / 2)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

ll N, K;

pair<ll, ll> solve()
{
    ll n = 1;
    map<ll, ll, greater<ll>> cnt;
    cnt[N] = 1;
    while (n < K) 
    {
       map<ll, ll, greater<ll>> tmp;
       for (auto it = cnt.begin(); it != cnt.end(); ++it)
       {
           ll k = it->st, v = it->nd;
           // printf("%lld:%lld ", k, v);
           if (k % 2 == 1) tmp[k / 2] += v * 2;
           else {
               tmp[k / 2] += v;
               tmp[k / 2 - 1] += v;
           }
       }
       cnt = tmp;
       K -= n;
       n *= 2;
    }
    // printf("\nK:%lld, n:%lld  \n", K, n);
    for (auto it = cnt.begin(); it != cnt.end(); ++it)
    {
        ll k = it->st, v = it->nd;
        // printf("%lld:%lld ", k, v);
        if (v >= K) 
        {
            return pair<ll,ll>(k / 2, k - k / 2 - 1);
        }
        K -= v;
    }

    return pair<ll, ll>(-1ll, -1ll);
}
int main()
{
    freopen("C-large.bin", "r", stdin);
    freopen("C-large.sol", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%lld%lld", &N, &K);
        pair<ll, ll> res = solve();
        printf("Case #%d: %lld %lld\n", t, res.st, res.nd);
    }
}

