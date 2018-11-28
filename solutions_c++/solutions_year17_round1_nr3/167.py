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

typedef long long i64;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<int> vi;
typedef vector<i64> vi64;
typedef vector<vi> vvi;
typedef vector<vi64> vvi64;
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

const i64 inf = 1e9+ 100500;

int f(int ih, int hd, int ad, int hk, int ak, int b, int d);

int g(int ih, int hd, int ad, int hk, int ak, int b, int d) {
  if (hk > 0) return f(ih, hd-ak, ad, hk, ak, b, d);
  return 0;
}

typedef tuple<int,int,int,int,int,int,int> t7;
std::map<t7, int> M;

int f(int ih, int hd, int ad, int hk, int ak, int b, int d) {
  // std::cerr << "f " << ih << ' ' << hd << ' ' << ad << ' ' << hk << ' ' << ak << ' ' << b << ' ' << d << '\n';
  if (hd <= 0) return inf;
  auto pit = M.insert(mp(t7(ih,hd,ad,hk,ak,b,d), inf));
  if (pit.se) {
    int ans = inf;
    uin(ans, g(ih,hd,ad,hk-ad,ak,b,d));
    if (ak>0) uin(ans, g(ih,hd,ad,hk,max(0,ak-d),b,d));
    if (ans != inf) pit.fi->se = ans + 1;
    uin(ans, g(ih,ih,ad,hk,ak,b,d));
    if (ans != inf) pit.fi->se = ans + 1;
    if (ad<hk) uin(ans, g(ih,hd,ad+b,hk,ak,b,d));
    if (ans != inf) pit.fi->se = ans + 1;
  }
  return pit.fi->se;
}

void solve(int ) {
  int hd, ad, hk, ak, b, d;
  hd = 1 + rand()%100;
  ad = 1 + rand()%100;
  hk = 1 + rand()%100;
  ak = 1 + rand()%100;
  b = 1 + rand()%100;
  d = 1 + rand()%100;
  cin >> hd >> ad >> hk >> ak >> b >> d;
  int r = f(hd,hd,ad,hk,ak,b,d);
  if (r == inf) cout << "IMPOSSIBLE\n";
  else cout << r << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout << fixed; cout.precision(15);
  cerr << fixed; cerr.precision(15);
#ifdef HOME
  freopen("input.txt", "r", stdin);
#endif
  int T;
  cin >> T;
  // T = 100;
  fore(t, 1, T) {
    cout << "Case #" << t << ": ";
    solve(t);
  }
  return 0;
}

