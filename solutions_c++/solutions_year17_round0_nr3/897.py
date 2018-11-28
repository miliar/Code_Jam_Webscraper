#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>

#define ull unsigned long long
#define mo 1000000007

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

//ll moMul(ll a, ll b) {
//    return ((a % mo) * (b % mo)) % mo;
//}
map<pll, pll> dp;

pll solve(ll n, ll k) {
    if (k == 1) return pll(n / 2, (n - 1) / 2);
    if (k == 2) return solve(n / 2, k / 2);
    if (dp.find(pll(n, k)) != dp.end()) return dp[pll(n, k)];
    pll l = solve((n - 1) / 2, (k - 1) / 2);
    pll r = solve(n / 2, k / 2);
    if (r.second < l.second || (r.second == l.second && r.first < l.first)) return dp[pll(n, k)] = r;
    return dp[pll(n, k)] = l;
}

int main() {
    freopen("/Users/Swing/Documents/code/googleCodeJam/C-large.in", "r", stdin);
    freopen("/Users/Swing/Documents/code/googleCodeJam/C-large.out", "w", stdout);

    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        ll n, k;
        cin >> n >> k;
        pll res = solve(n, k);
        cout << res.first << " " << res.second << endl;
//        printf("Case #%d: %.8f\n", i, res);
//        cout << "Case #" << i << ": " << tmp << endl;
//        printf("Case #%d: %.7lf\n", i, res);

    }

    return 0;
}