#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll solve(ll n, ll k) {
    multiset<ll> s;
    s.insert(n);
    for (int i = 0; i < k-1; i++) {
        ll cur = *s.rbegin();
        s.erase(s.find(cur));
        s.insert((cur - 1) / 2);
        s.insert(cur / 2);
    }
    return *s.rbegin();
}

ll solve2(ll n, ll k) {
    map<ll, ll> m;
    ll cnt = 0;
    m[n] = 1;
    while (true) {
        pair<ll, ll> cur = *m.rbegin();
        cnt += cur.second;
        if (cnt >= k) {
            break;
        }
        m.erase(cur.first);
        m[cur.first / 2] += cur.second;
        m[(cur.first - 1) / 2] += cur.second;
    }
    return (*m.rbegin()).first;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        ll n, k;
        cin >> n >> k;
        ll res = solve2(n, k);
        cout << res / 2 << " " << (res - 1) / 2  << endl;
    }
    return 0;
}