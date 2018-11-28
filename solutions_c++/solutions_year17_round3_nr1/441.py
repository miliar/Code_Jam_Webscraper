#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
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

const int N = 1000 + 3;

int n, k;
pti p[N];

bool read() {
    if (scanf("%d%d", &n, &k) != 2) return false;
    forn(i, n) assert(scanf("%d%d", &p[i].x, &p[i].y) == 2);
    return true;
}

void solve() {
    ld ans = 0;
    forn(i, n) {
        ld cur = PI * sqr(ld(p[i].x)) + 2 * PI * p[i].x * ld(p[i].y);
        vector<ld> hs;
        forn(j, n) if (p[j].x <= p[i].x && j != i) {
            hs.pb(2.0 * PI * p[j].x * ld(p[j].y));
        }
        sort(all(hs));
        reverse(all(hs));
        if (sz(hs) >= k - 1) {
            forn(j, k - 1) cur += hs[j];
            ans = max(ans, cur);
        }
    }
    cout << ans << endl;
}

int main() {
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

    int testCount;
    cin >> testCount;

    forn(test, testCount) {
        ld stime = gett();
        read();
        printf("Case #%d: ", test + 1);
        solve();
        cerr << "Time: " << gett() - stime << endl;
    }
    
    return 0;
}

