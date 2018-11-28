#define DBG 1

#include <cstring>
#include <map>
#include <unordered_map>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> pii;

int gi() {
    int a;
    scanf("%d", &a);
    return a;
}

ll gli() {
    ll a;
    scanf("%lld", &a);
    return a;
}

void inc(map<ll, ll> &m, ll k, ll v) {
    map<ll, ll>::iterator it = m.find(k);
    if (it == m.end())
        m[k] = v;
    else
        it->second += v;
}

#define SINGLELINE 1
void solve() {
    ll n = gli();
    ll k = gli();

    map<ll, ll> m;
    m[n] = 1;

    while (1) {
        map<ll, ll>::iterator it = m.end();
        it--;
        ll key = it->first;
        ll val = it->second;
        m.erase(it);

        ll mn = (key - 1LL) / 2LL;
        ll mx = key / 2LL;

        if (val >= k) {
            printf("%lld %lld\n", mx, mn);
            return;
        }

        k -= val;
        inc(m, mx, val);
        if (mn)
            inc(m, mn, val);
    }
}

int main() {
    int t = gi();

    for (int i = 1; i <= t; i++) {
        printf("Case #%d:%c", i, (SINGLELINE ? ' ' : '\n'));
        solve();
        fprintf (stderr, "Case %d / %d. Elapsed %.2f. Estimated %.2f\n", i, t, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * t) / CLOCKS_PER_SEC);
    }

    return 0;
}
