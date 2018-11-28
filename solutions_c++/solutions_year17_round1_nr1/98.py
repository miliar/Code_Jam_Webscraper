#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define all(x) x.begin(), x.end()
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define debug(x) std::cerr << "DEBUG: " << #x << " = " << x << std::endl

template<typename T>
inline void mn(T& x, const T& y) { x = std::min(x, y); }
template<typename T>
inline void mx(T& x, const T& y) { x = std::max(x, y); }
template<typename T>
inline int sz(const T& t) { return static_cast<int>(t.size()); }

void solve() {
  int r, c;
  std::cin >> r >> c;
  std::vector<std::string> f(r);
  forn (i, r) {
    std::cin >> f[i];
  }

  std::vector<int> cols;
  forn (i, r)  {
    forn (j, c) {
      if (f[i][j] != '?') {
        cols.push_back(j);
      }
    }
  }
  cols.push_back(-1);
  std::sort(all(cols));
  cols.erase(std::unique(all(cols)), cols.end());
  cols.back() = c - 1;

  for (int x = 0; x + 1 < sz(cols); ++x) {
    std::vector<int> rows;
    std::vector<char> order;
    forn (i, r) {
      for (int j = cols[x] + 1; j <= cols[x + 1]; ++j) {
        if (f[i][j] != '?') {
          order.push_back(f[i][j]);
          rows.push_back(i);
        }
      }
    }
    rows.push_back(-1);
    std::sort(all(rows));
    rows.erase(std::unique(all(rows)), rows.end());
    rows.back() = r - 1;

    for (int y = 0; y + 1 < sz(rows); ++y) {
      for (int i = rows[y] + 1; i <= rows[y + 1]; ++i) {
        for (int j = cols[x] + 1; j <= cols[x + 1]; ++j) {
          f[i][j] = order[y];
        }
      }
    }
  }


  std::cout << "\n";
  forn (i, r) {
    std::cout << f[i] << "\n";
  }

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
