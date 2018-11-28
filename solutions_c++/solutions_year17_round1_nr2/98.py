#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <array>
#include <set>

#define all(x) x.begin(), x.end()
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define debug(x) std::cerr << "DEBUG: " << #x << " = " << x << std::endl

template<typename T>
inline void mn(T& x, const T& y) { x = std::min(x, y); }
template<typename T>
inline void mx(T& x, const T& y) { x = std::max(x, y); }
template<typename T>
inline int sz(const T& t) { return static_cast<int>(t.size()); }

int div_round_down(int x, int y) { return x / y; }
int div_round_up(int x, int y) { return (x + y - 1) / y; }

struct Package {
  int product;
  int package;
};

bool operator<(const Package& a, const Package& b) {
  return (a.product != b.product) ? (a.product < b.product) : (a.package < b.package);
}


void solve() {
  int n, p;
  std::cin >> n >> p;

  std::vector<int> r(n);
  forn (i, n) {
    std::cin >> r[i];
  }

  std::vector<std::vector<int>> q(n, std::vector<int>(p));
  forn (i, n) {
    forn (j, p) {
      std::cin >> q[i][j];
    }
  }

  const int ADD = 0;
  const int DEL = 1;

  std::map<int, std::array<std::vector<Package>, 2>> m;

  std::vector<std::vector<std::pair<int, int>>> a(n, std::vector<std::pair<int, int>>(p));
  forn (i, n) {
    forn (j, p) {
      a[i][j].first = std::max(1, div_round_up(q[i][j] * 100, 110 * r[i]));
      a[i][j].second = div_round_down(q[i][j] * 100, 90 * r[i]);
      if (a[i][j].first <= a[i][j].second) {

        m[a[i][j].first][ADD].push_back(Package{i, j});
        m[a[i][j].second + 1][DEL].push_back(Package{i, j});
      }
//      debug(a[i][j].first);
//      debug(a[i][j].second);
//      x <= (q[i][j] * 100) / (90 * r[i]);
//      y >= (q[i][j] * 100) / (110 * r[i])
    }
  }

  std::vector<std::set<std::pair<int, int> > > cnt(n);
  int ans = 0;
  for (const auto& e : m) {
    for (auto x : e.second[ADD]) cnt[x.product].insert({a[x.product][x.package].second, x.package});
    for (auto x : e.second[DEL]) cnt[x.product].erase( {a[x.product][x.package].second, x.package});

    int make = std::numeric_limits<int>::max();
    for (const auto& s : cnt) {
      mn(make, sz(s));
    }
    ans += make;
    for (auto& s : cnt) {
      for (int i = 0; i < make; ++i) {
        s.erase(s.begin());
      }
    }
  }
  std::cout << ans << std::endl;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int t;
  std::cin >> t;
//  debug(t);
  for (int i = 0; i < t; ++i) {
    std::cout << "Case #" << (i + 1) << ": ";
    solve();
  }
  std::cout.flush();
  return 0;
}
