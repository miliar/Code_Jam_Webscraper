#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }
inline ll getll() { unsigned int c; ll x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getll(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

pair<ll, ll> get(ll n) {
    n--;
    const auto m = n >> 1;
    if (n & 1) return make_pair(m, m + 1);
    return make_pair(m, m);
}

void solve_case() {
    const ll n = getll();
    ll k = getll(), t;
    map<ll, ll, greater<ll>> intervals;
    ll res1, res2;
    intervals[n] = 1LL;
    ll operation_count = 0LL;
    while (1) {
        const auto p = *intervals.begin();
        auto t = get(p.first);
        res1 = t.first, res2 = t.second;
        const auto m = p.second;
        operation_count += m;
        intervals[res1] += m;
        intervals[res2] += m;
        intervals.erase(p.first);
        if (operation_count >= k) break;
    }
    cout << res2 << " " << res1 << endl;
    return;
}

int main () {
    int test_count, test_case = getint();
    for (test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
