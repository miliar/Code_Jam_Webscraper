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

string s;

bool read() {
    cin >> s;
    return true;
}

void solve() {
    while (true) {
        int idx = 0;
        while (idx < sz(s) - 1 && s[idx] <= s[idx + 1]) idx++;
        if (idx == sz(s) - 1) {
            puts(s.c_str());
            return;
        }
        for (int i = idx + 1; i < sz(s); i++) {
            s[i] = '9';
        }
        s[idx]--;
        while (s[0] == '0') {
            s.erase(s.begin());
        }
    }
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

