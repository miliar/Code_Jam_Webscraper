#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define ford1(i, n) for(int i = (int)(n); i>=1; --i)
#define fored(i, a, b) for(int i = (int)(b); i >= (int)(a); --i)
#define sz(v) ((int)((v).size()))
#define all(v) (v).begin(), (v).end()
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

const int inf = 1e9 + 100500;
const int N = 25;

void init() {
  vi a(N+1);
  a[0] = 1;
  a[1] = 1;
  fore(i, 2, N) {
    fore(j, 1, i) a[i] += a[i-j];
  }
}


void solve() {
  int n, m;
  cin >> n >> m;
  vs a(n);
  forn(i, n) cin >> a[i];
  forn(i, n) forn(j, m) if (j && a[i][j-1]!='?' && a[i][j] == '?') a[i][j] = a[i][j-1];
  forn(i, n) ford(j, m) if (j && a[i][j-1]=='?' && a[i][j] != '?') a[i][j-1] = a[i][j];

  forn(i, n) forn(j, m) if (i && a[i-1][j]!='?' && a[i][j] == '?') a[i][j] = a[i-1][j];
  ford(i, n) forn(j, m) if (i && a[i-1][j]=='?' && a[i][j] != '?') a[i-1][j] = a[i][j];

  forn(i, n) cout << a[i] << '\n';
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
    cout << "Case #" << t << ":\n";
    solve();
  }
  return 0;
}

