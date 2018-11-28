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

li n, k;

bool read() {
	return !!(cin >> n >> k);
}

li len;
map<li, li> z;

li solve(li n) {
  if (n < len) return 0;
  if (z.count(n)) return z[n];
  li& ans = z[n];
  ans = 1;
  ans += solve(n >> 1);
  ans += solve((n - 1) >> 1);
#ifdef LOG
  clog << "n: " << n << " ans: " << ans << endl;
#endif
  return ans;
}

li calc(auto len) {
  z.clear();
  ::len = len;
#ifdef LOG
  clog << "len: " << len << endl;
#endif
  return solve(n);
}

void solve(int tt) {
  /*len = 0;
  calc(n);
  exit(0);*/

  printf("Case #%d: ", tt + 1);
  li lf = 1, rg = n;
  while (lf != rg) {
    li md = (lf + rg + 1) >> 1;
    li cnt = calc(md);
    if (cnt >= k) lf = md;
    else rg = md - 1;
  }

#ifdef LOG
  clog << "lf: " << lf << " calc(lf): " << calc(lf) << endl;
  //exit(0);
#endif


  assert(calc(lf) >= k);
  assert(calc(lf + 1) < k);
  printf("%lld %lld\n", lf >> 1, (lf - 1) >> 1);
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
