#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

li n, k;

bool read() {
    cin >> n >> k;
    return true;
}

pair<li, li> naive(li n, li k) {
    vector<bool> used(n + 2);
    used[0] = used[sz(used) - 1] = true;
    forn(iter, k) {
        vector<int> dlf(sz(used), 0), drg(sz(used), 0);
        forn(i, sz(used)) {
            if (!used[i]) dlf[i] = dlf[i - 1] + 1;
        }
        nfor(i, sz(used)) {
            if (!used[i]) drg[i] = drg[i + 1] + 1;
        }
        int best = -1, mind = -INF, maxd = -INF;
        forn(i, sz(used)) {
            if (used[i]) continue;
            int cmind = min(dlf[i], drg[i]);
            int cmaxd = max(dlf[i], drg[i]);
            if (cmind > mind || (cmind == mind && cmaxd > maxd)) {
                mind = cmind; maxd = cmaxd; best = i;
            }
        }
        used[best] = true;
        if (iter == k - 1) return mp(maxd - 1, mind - 1);
    }
    throw;
}

void solve() {
    li on = n, ok = k;

    vector<li> len, cnt;
    len.pb(n);
    cnt.pb(1);
    forn(i, sz(len)) {
        li n1 = len[i] / 2, n2 = (len[i] - 1) / 2;
        if (n1 != 0) {
            if (len.back() != n1) {
                len.pb(n1);
                cnt.pb(0);
            }
            cnt.back() += cnt[i];
        }
        if (n2 != 0) {
            if (len.back() != n2) {
                len.pb(n2);
                cnt.pb(0);
            }
            cnt.back() += cnt[i];
        }
    }
    pair<li, li> res;
    forn(i, sz(len)) {
        if (cnt[i] >= k) {
            res = mp(len[i] / 2, (len[i] - 1) / 2);
            break;
        }
        k -= cnt[i];
    }
    cout << res.first << ' ' << res.second << endl;
    return;

    pair<li, li> ans = naive(on, ok);
    if (res != ans) {
        cerr << "test = " << on << ' ' << ok << endl;
        cerr << "res = " << res << endl;
        cerr << "ans = " << ans << endl;
        //throw;
    }
}

int main() {
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

    /*forl(nn, 100) {
        forl(kk, nn) {
            n = nn; k = kk;
            solve();
        }
    }
    return 0;*/

    int testCount;
    assert(scanf("%d", &testCount) == 1);
    forl(test, testCount) {
        ld stime = gett();
        printf("Case #%d: ", test);
        read();
        solve();
        cerr << "Test = " << test << "; time: " << gett() - stime << endl;
        //break;
    }
    
    return 0;
}

