#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back
#define eb emplace_back

#define fi first
#define se second

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<ld, ld> pld;
typedef vector<ld> vld;
typedef vector<pld> vpld;

const ld eps = 1e-9;
const ld pi = acosl(-1.0);

template<typename T> bool uin(T& a, T b) { if (b < a) { a = b; return true; } return false; }
template<typename T> bool uax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

bool can(const vi &a, int m, int&mv) {
  mv = 0;
  int x = 0;
  ford(i, a.size()) {
    x += a[i];
    x -= m;
    uax(x, 0);
    mv += max(0, a[i] - m);
  }
  return x <= 0;
}

void solve() {
  int n, c, m;
  cin >> n >> c >> m;
  vi by_c(c, 0);
  vi by_n(n, 0);
  forn(i, m) {
    int pi, bi;
    cin >> pi >> bi;
    by_c[bi-1] += 1;
    by_n[pi-1] += 1;
  }
  int L = *max_element(all(by_c)) - 1, R = m, rmv = -1;
  // cerr << n << ' ' << c << ' ' << m << '\n'; cerr << L << ' ' << R << '\n';
  while (R-L>1) {
    int M = (L+R+1)/2;
    int cmv = -1;
    if (can(by_n, M, cmv)) { R = M;
      // cerr << L << ' ' << R << '+' << cmv << '\n';
    } else { L = M; 
      // cerr << L << ' ' << R << '-' << cmv << '\n';
    }
  }
  bool ok = can(by_n, R, rmv);
  // assert(ok);
  cout << R << ' ' << rmv << '\n';
}

int main() {
#ifdef HOME
  // freopen("input.txt", "r", stdin);
#endif
  // init();
  cout << fixed;
  cout.precision(15);
  int T;
  // cerr << can({2, 0}, 1, T) << ' ' << T << '\n'; return 0;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
