#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <numeric>


class farther {
  public:
    farther (int n) : _n(n) {}
    bool operator() (const int x, const int y) {
      return abs(x-_n+1) > abs(y-_n+1);
    }
    int _n;
};

int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    int n, m;
    std::cin >> n >> m;
    std::set<std::pair<int, int>> origp;
    std::set<std::pair<int, int>> origx;
    std::set<int> row;
    std::set<int> column;
    std::set<int> diagplus;
    std::set<int> diagminus;
    int style = 0;
    for (int i = 0; i < m; ++i) {
      char c;
      int x, y;
      std::cin >> c >> x >> y;
      --x;
      --y;
      if (c == '+') {
        origp.insert({x, y});
        diagplus.insert(x+y);
        diagminus.insert(x-y);
        ++style;
      }
      else if (c == 'x') {
        origx.insert({x, y});
        row.insert(x);
        column.insert(y);
        ++style;
      }
      else if (c == 'o') {
        row.insert(x);
        column.insert(y);
        diagplus.insert(x+y);
        diagminus.insert(x-y);
        ++style;
        ++style;
      }
    }
    std::set<std::pair<int, int>> newp;
    std::set<std::pair<int, int>> newx;
    for (int x = 0; x < n; ++x) {
      if (row.count(x) != 0)
        continue;
      for (int y = 0; y < n; ++y) {
        if (column.count(y) != 0)
          continue;
        newx.insert({x, y});
        row.insert(x);
        column.insert(y);
        ++style;
        break;
      }
    }
    std::vector<int> sums(2*n-1);
    std::iota(sums.begin(), sums.end(), 0);
    std::sort(sums.begin(), sums.end(), farther(n));
    for (int sum : sums) {
      if (diagplus.count(sum) != 0)
        continue;
      for (int x = 0; x < n; ++x) {
        int y = sum - x;
        if (y < 0 || y >= n)
          continue;
        if (diagminus.count(x-y) != 0)
          continue;
        newp.insert({x, y});
        diagplus.insert(x+y);
        diagminus.insert(x-y);
        ++style;
        break;
      }
    }
    int newmodels = newp.size() + newx.size();
    for (auto coord : newp)
      if (newx.count(coord) != 0)
        --newmodels;
    std::cout << "Case #" << t+1 << ": " << style << " " << newmodels << std::endl;
    for (auto coord : newp) {
      if (newx.count(coord) != 0)
        continue;
      if (origx.count(coord) == 0)
        std::cout << "+ " << coord.first+1 << " " << coord.second+1 << std::endl;
      else
        std::cout << "o " << coord.first+1 << " " << coord.second+1 << std::endl;
    }
    for (auto coord : newx) {
      if (origp.count(coord) == 0 && newp.count(coord) == 0)
        std::cout << "x " << coord.first+1 << " " << coord.second+1 << std::endl;
      else
        std::cout << "o " << coord.first+1 << " " << coord.second+1 << std::endl;
    }
  }
  return EXIT_SUCCESS;
}
