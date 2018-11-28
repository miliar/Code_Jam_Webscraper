#include <iostream>
#include <set>

using namespace std;

const int MAXN = 1e6+2;

struct cell {
  int id, l, r;
  bool operator<(const cell& c) const {
    if (min(l, r) == min(c.l, c.r)) {
      if (max(l, r) == max(c.l, c.r))
        return id < c.id;
      return max(l, r) > max(c.l, c.r);
    }
    return min(l, r) > min(c.l, c.r);
  }
};

set<cell> cells;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n, k;
    cin >> n >> k;
    cells.clear();
    cells.insert({(n - 1) / 2, (n - 1) / 2, n - (n - 1) / 2 - 1});
    for (int i = 0; i < k - 1; ++i) {
      cell cur = *cells.begin();
      cells.erase(cur);
      int a = cur.id - cur.l - 1;
      int b = cur.id;
      int c = cur.id + cur.r + 1;
      int x = (a + b) / 2;
      int y = (b + c) / 2;
      if (a != x && x != b)
        cells.insert({x, x - a - 1, b - x - 1});
      if (b != y && y != c)
        cells.insert({y, y - b - 1, c - y - 1});
    }
    cell cur = (cells.empty() ? (cell){0, 0, 0} : *cells.begin());
    cout << "Case #" << t << ": ";
    cout << max(cur.l, cur.r) << " ";
    cout << min(cur.l, cur.r) << endl;
  }
  return 0;
}