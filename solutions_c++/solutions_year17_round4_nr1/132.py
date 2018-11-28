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

const int N = 100 + 3;

int n, p;
int a[N];
int d[N][N][N];

bool read() {
    if (scanf("%d%d", &n, &p) != 2) return false;
    forn(i, n) assert(scanf("%d", &a[i]) == 1);
    return true;
}

int calc(int r1, int r2, int r3) {
    int& ans = d[r1][r2][r3];
    if (ans != -1) return ans;
    ans = 0;
    forn(i1, p + 1) {
        if (i1 > r1) break;
        forn(i2, p + 1) {
            if (i2 > r2) break;
            forn(i3, p + 1) {
                if (i3 > r3) break;
                if (i1 == 0 && i2 == 0 && i3 == 0) continue;
                int val = calc(r1 - i1, r2 - i2, r3 - i3);
                if ((i1 + 2 * i2 + 3 * i3) % p == 0 && (r1 != i1 || r2 != i2 || r3 != i3)) val++;
                ans = max(ans, val);
            }
        }
    }
    //cerr << r1 << ' ' << r2 << ' ' << r3 << ' ' << ans << endl;
    return ans;
}

void solve() {
    int ans = 1;
    memset(d, -1, sizeof(d));
    vector<int> rem(4, 0);
    forn(i, n) {
        if (a[i] % p == 0) ans++;
        else rem[a[i] % p]++;
    }
    //cerr << rem << endl;
    if (ans == n + 1) ans = n;
    else ans += calc(rem[1], rem[2], rem[3]);
    cout << ans << endl;
}

int main() {
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

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

