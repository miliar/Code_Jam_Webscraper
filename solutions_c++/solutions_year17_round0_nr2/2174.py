#include <bits/stdc++.h>
#include <experimental/optional>

#define FORE(i, c) for (auto& i : (c))
#define FOR(i, j, k) for (int i = (j); i < (k); ++i)
#define REP(i, j) FOR(i, 0, j)
#define ALL(v) begin(v), end(v)
#define pb push_back
#define _1 first
#define _2 second
#define vec vector

using namespace std;
using namespace std::experimental;

typedef long long ll; typedef vec<int> vi; typedef vec<ll> vll; typedef pair<ll, ll> pll; typedef pair<int, int> pii;
template <typename T, typename U> inline void amin(T& x, U y) { if (y < x) x = y; }
template <typename T, typename U> inline void amax(T& x, U y) { if (y > x) x = y; }
template <typename C, typename V> inline bool in(const C& c, const V& v) { return c.find(v) != c.end(); }
template <typename T> inline bool in(const vec<T>& v, const T& t) { return find(ALL(v), t) != end(v); }
template <typename T> inline T sq(T t) { return t * t; }

optional<string> solve(string s, int i, int lo, bool flag = false) {
    if (i == s.length()) return string();
    int hi = flag ? 9 : s[i] - '0';
    if (hi < lo) return nullopt;
    for (int x = hi - lo; x >= 0; --x) {
        if (auto s2 = solve(s, i+1, lo + x, flag || x != hi - lo))
            return to_string(lo + x) + *s2;
    }
    return nullopt;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        cout << "Case #" << Case << ": ";
        string s;
        cin >> s;
        auto x = solve(s, 0, 1);
        if (x) cout << *x;
        else REP(i, s.length() - 1) cout << 9;
        cout << endl;
    }
    return 0;
}

