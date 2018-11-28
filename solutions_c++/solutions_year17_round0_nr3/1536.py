#include <bits/stdc++.h>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;

int main()
{
#ifdef PIT
freopen("C-large.in", "r", stdin);
freopen("C-large.out", "w", stdout);
#endif // PIT
    int ic = 1, T;
    for(scanf("%d", &T); ic <= T; ++ic){
        printf("Case #%d: ", ic);
        ll n, k;
        scanf("%I64d %I64d", &n, &k);
        /**
        priority_queue<ll > pq;
        while(!pq.empty()) pq.pop();
        pq.push(n);
        ll x, y, z;
        for(int i = 0; i < k; ++i) {
            z = pq.top(); pq.pop();
            x = (1+z) / 2, y = z - x + 1;
            if(x == y) pq.push(--x), pq.push(y = x);
            else pq.push(y = x), pq.push(--x);
        }
        printf("%I64d %I64d\n", y, x);
        **/
        ll t, s;
        for(t = 1LL; t < k; t <<= 1) n -= t, k -= t;
        s = n / t;
        if(k <= n % t) ++s;
        printf("%I64d %I64d\n", s/2, (s-1)/2);
    }
    return 0;
}
/**
0.48.2.59.1.6a.3.7b.0
**/
