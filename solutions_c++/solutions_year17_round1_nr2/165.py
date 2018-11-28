#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define ford1(i, n) for(int i = (int)(n); i>=1; --i)
#define fored(i, a, b) for(int i = (int)(b); i >= (int)(a); --i)
#define sz(v) ((int)((v).size()))
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define fi first
#define se second

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<ld> vld;
typedef vector<string> vs;

template<class T> T sqr(const T& a) { return a * a; }
template<class T> bool uax(T&a, const T& b) { if( a < b ) { a = b; return true; } return false; }
template<class T> bool uin(T&a, const T& b) { if( a > b ) { a = b; return true; } return false; }

#ifdef HOME
#define dbg(v) do {cerr << v << '\n';}while(0)
#else
#define dbg(v) do {;}while(0)
#endif

const int inf = 1e6 + 100500;
const int N = 25;

void init() {
}


void solve(int ) {
  int n, m;
  cin >> n >> m;
  vi r(n);
  forn(i, n) cin >> r[i];
  vvi a(n, vi(m));
  forn(i, n) forn(j, m) cin >> a[i][j];
  forn(i, n) sort(rall(a[i]));
  int ans = 0;
  fore(c, 1, inf) {
    if (*max_element(all(r))*c>=inf) break;
    int cans = 1;
    forn(i, n) {
      int val = c * r[i];
      while (!a[i].empty() && a[i].back()*10<val*9) a[i].pop_back();
      if (a[i].empty() || a[i].back()*10>val*11) cans = 0;
    }
    if (cans) {
      ans += cans;
      forn(i, n) a[i].pop_back();
      c -= 1;
    }
  }
  cout << ans << '\n';
}

void solve2(int test) {
  int n, m;
  cin >> n >> m;
  vi r(n);
  forn(i, n) cin >> r[i];
  vvi a(n, vi(m));
  forn(i, n) forn(j, m) cin >> a[i][j];
  // if (test != 35) { cout << '\n'; return ; }
  forn(i, n) sort(rall(a[i]));
  int ans = 0;
  assert(n <= 2);
  do {
    int cans = 0;
    forn(j, m) {
      int cl = 1, cr = inf;
      forn(i, n) {
        uax(cl, int(a[i][j] * 10 / 11. / r[i] - 10));
        uin(cr, int(a[i][j] * 10 / 9. / r[i] + 10));
        while (cl <= cr && r[i] * cl * 11 < a[i][j] * 10) ++cl;
        while (cl <= cr && r[i] * cr * 9 > a[i][j] * 10) --cr;
      }
      // cerr << j << ' ' << cl << ' ' << cr << '\n';
      if (cl <= cr) {
        cans += 1;
      }
    }
    // forn(i, n) forn(j, m) cerr << a[i][j] << " \n"[j+1==m]; cerr << cans << '\n';
    uax(ans, cans);
  } while (n > 1 && next_permutation(rall(a[1])));
  cout << ans << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout << fixed; cout.precision(15);
  cerr << fixed; cerr.precision(15);
#ifdef HOME
  freopen("input.txt", "r", stdin);
#endif
  init();
  int T;
  cin >> T;
  fore(t, 1, T) {
    cout << "Case #" << t << ": ";
    solve(t);
  }
  return 0;
}

