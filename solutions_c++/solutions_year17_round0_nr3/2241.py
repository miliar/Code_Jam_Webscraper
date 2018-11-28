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

map<ll, ll> update(const map<ll, ll>& counts) {
    map<ll, ll> newCounts;
    FORE(p, counts) {
        ll sp = p._1 - 1;
        assert(sp >= 0);
        if (sp / 2)
            newCounts[sp / 2] += p._2;
        if (sp)
            newCounts[(sp - 1) / 2 + 1] += p._2;
    }
    return newCounts;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    FOR(Case, 1, T+1) {
        cout << "Case #" << Case << ": ";

        ll N, K;
        cin >> N >> K;
        map<ll, ll> counts {{N, 1}};
        ll z = 1;
        while (K > z) {
            counts = update(counts);
            K -= z;
            z <<= 1;
        }

        assert(K > 0);
        ll sp;
        while (true) {
            assert(!counts.empty());
            auto it = max_element(ALL(counts));
            if (it->_2 < K) {
                K -= it->_2;
                counts.erase(it);
                continue;
            }
            sp = it->_1 - 1;
            break;
        }

        ll lo;
        if (sp == 0) lo = 0;
        else lo = (sp - 1) / 2 + 1;
        cout << lo << " " << sp / 2;
        cout << endl;
    }
    return 0;
}

