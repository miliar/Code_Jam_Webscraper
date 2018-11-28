#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int n, m;
    cin >> n >> m;
    bool flag = false;
    int tx = -1, ty = -1;
    set<pair<int, int>> se;
    for (int i = 0; i < m; i++) {
      char c;
      int x, y;
      cin >> c >> x >> y;
      if (c == '+') {
        se.insert({x, y});
      } else {
        se.insert({x, y});
        tx = x, ty = y;
        flag |= (c == 'o');
      }
    }
    printf("Case #%d: ", cas);
    if (n == 1) {
      if (!flag) {
        printf("2 1\no 1 1\n");
      } else {
        printf("2 0\n");
      }
    } else {
      printf("%d ", 3 * n - 2);
      vector<pair<char, pair<int, int>>> vec;
      if (tx == -1) {
        if (se.size() == n) {
          vec.push_back({'o', {1, 1}});
          tx = ty = 1;
          flag = true;
          se.insert({1, 1});
        } else {
          for (int i = 1; i <= n; i++) {
            if (!se.count({1, i})) {
              tx = 1, ty = i;
              flag = true;
              vec.push_back({'o', {1, i}});
              se.insert({1, i});
              break;
            }
          }
        }
      }
      if (!flag) {
        vec.push_back({'o', {tx, ty}});
      }
      int nx = tx + 1, ny = ty - 1;
      while (ny > 0) {
        vec.push_back({'x', {nx++, ny--}});
      }
      ny = ty + 1;
      while (ny <= n) {
        vec.push_back({'x', {nx++, ny++}});
      }
      for (int i = 1; i <= n; i++) {
        if (!se.count({1, i})) {
          vec.push_back({'+', {1, i}});
        }
      }
      for (int i = 2; i <= n - 1; i++) {
        vec.push_back({'+', {n, i}});
      }
      cout << vec.size() << endl;
      for (auto x : vec) {
        cout << x.first << " " << x.second.first << " " << x.second.second
             << endl;
      }
    }
  }
  return 0;
}
