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

map<vi, int> M;

int go(vi a) {
  auto pit = M.emplace(a, 0);
  if (pit.se) {
    int r = 0, p = a[a.size() - 2];
    bool any = false;
    forn(i, a.size() - 2) if (a[i]) {
      any = true;
      vi b(a); b[i] -= 1;
      b.back() = (b.back() + i) % p;
      uax(r, go(b));
    }
    if (a.back() == 0 && any) r += 1;
    pit.fi->se = r;
  }
  return pit.fi->se;
}

void solve() {
  int n, p;
  cin >> n >> p;
  vi a(p + 2, 0);
  a[p] = p;
  forn(i, n) {
    int x;
    cin >> x;
    a[x%p] += 1;
  }
  cout << go(a) << '\n';
}

int main() {
#ifdef HOME
  // freopen("input.txt", "r", stdin);
#endif
  // init();
  cout << fixed;
  cout.precision(15);
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
