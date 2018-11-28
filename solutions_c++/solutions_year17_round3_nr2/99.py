#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,m;
    cin >> n >> m;
    const int T = 24 * 60;
    const int SHIFT = 12 * 60;
    vector<vector<int>> can(2, vector<int>(T, true));
    for (int i = 0; i < n; ++i) {
      int x, y;
      cin >> x >> y;
      for (int j = x; j < y; ++j) {
        can[0][j] = false;
      }
    }
    for (int i = 0; i < m; ++i) {
      int x, y;
      cin >> x >> y;
      for (int j = x; j < y; ++j) {
        can[1][j] = false;
      }
    }

    int ans = T + 1;
    for (int who_first = 0; who_first < 2; ++who_first) {
      vector<vector<vector<int>>> d(2, vector<vector<int>>(T + 1, vector<int>(SHIFT + 1, T)));

      if (can[who_first][0]) {
        d[who_first][0][0] = 0;
      } else {
        continue;
      }

      for (int i = 0; i <T; ++i) {
        for (int j = 0; j <= SHIFT; ++j) {
          for (int who_now = 0; who_now < 2; ++who_now) {
            for (int who_next = 0; who_next < 2; ++who_next) {
              if (!can[who_next][i]) continue;
              if (j == SHIFT && who_next == 0) continue;
              int a = d[who_now][i][j];
              if (a == T) continue;
              if (who_now != who_next) a++;
              int add = who_next == 0 ? 1 : 0;
              d[who_next][i+1][j + add] = min(d[who_next][i+1][j + add], a);
            }
          }
        }
      }

      for (int who_finish = 0; who_finish < 2; ++who_finish) {
        ans = min(ans, d[who_finish][T][SHIFT] + (who_first != who_finish ? 1 : 0));
      }
    }

    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
