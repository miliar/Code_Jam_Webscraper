#include <bits/stdc++.h>

#define FORE(i, c) for (auto& i : (c))
#define FOR(i, j, k) for (int i = (j); i < (k); ++i)
#define REP(i, j) FOR(i, 0, j)
#define ALL(v) begin(v), end(v)
#define pb push_back
#define _1 first
#define _2 second
#define vec vector

using namespace std;

typedef long long ll; typedef vec<int> vi; typedef vec<ll> vll; typedef pair<ll, ll> pll; typedef pair<int, int> pii;
template <typename T, typename U> inline void amin(T& x, U y) { if (y < x) x = y; }
template <typename T, typename U> inline void amax(T& x, U y) { if (y > x) x = y; }
template <typename C, typename V> inline bool in(const C& c, const V& v) { return c.find(v) != c.end(); }
template <typename T> inline bool in(const vec<T>& v, const T& t) { return find(ALL(v), t) != end(v); }
template <typename T> inline T sq(T t) { return t * t; }

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        int R, C;
        char a[30][30];
        cin >> R >> C;
        REP(i, R) {
            string s;
            cin >> s;
            REP(j, C)
                a[i][j] = s[j] == '?' ? 0 : s[j];
        }
        FOR(i, 1, R) REP(j, C)
            if (a[i][j] == 0) a[i][j] = a[i-1][j];
        FOR(i, 1, R) REP(j, C)
            if (a[R-i-1][j] == 0) a[R-i-1][j] = a[R-i][j];
        FOR(j, 1, C) REP(i, R)
            if (a[i][j] == 0) a[i][j] = a[i][j-1];
        FOR(j, 1, C) REP(i, R)
            if (a[i][C-j-1] == 0) a[i][C-j-1] = a[i][C-j];
        cout << "Case #" << Case << ":" << endl;
        REP(i, R) {
            REP(j, C)
                cout << a[i][j];
            cout << endl;
        }
    }
    return 0;
}

