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
template<typename T> inline ostream& operator<< (ostream& out, const pair<T*, int>& a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
//#define LOG
#endif

const int N = 30;

int n, m;
string a[N];

bool read() {
  if (!(cin >> n >> m)) return false;
  forn(i, n) assert(cin >> a[i]);
	return true;
}

void solve(int tt) {
  printf("Case #%d:\n", tt + 1);

  int lasti = -1;
  forn(i, n) {
    int lastj = -1;
    forn(j, m)
      if (a[i][j] != '?') {
        fore(x, lasti + 1, i + 1)
          fore(y, lastj + 1, j + 1)
            a[x][y] = a[i][j];
        lastj = j;
      }
    if (lastj != -1) {
      forn(j, m)
        if (a[i][j] == '?') {
          assert(j > 0 && a[i][j - 1] != '?');
          fore(x, lasti + 1, i + 1)
            a[x][j] = a[i][j - 1];
        }
      lasti = i;
    }
#ifdef LOG
    clog << "i: " << i << " lasti: " << lasti << " lastj: " << lastj << endl;
#endif
  }

  forn(i, n)
    forn(j, m)
      if (a[i][j] == '?') {
        assert(i > 0 && a[i - 1][j] != '?');
        a[i][j] = a[i - 1][j];
      }

  forn(i, n) forn(j, m) assert(a[i][j] != '?');
  forn(i, n) printf("%s\n", a[i].c_str());
}

int main() {
#ifdef SU1
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
#endif

  cout << setprecision(10) << fixed;
  cerr << setprecision(5) << fixed;

  int tc;
  cin >> tc;
  forn(tt, tc) {
    cerr << "Case #" << tt + 1 << endl;
    assert(read());
    ld stime = gett();
    solve(tt);
    cerr << "Time: " << gett() - stime << endl;
    //break;
  }

  return 0;
}
