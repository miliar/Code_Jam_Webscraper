#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, p;
    cin >> n >> p;

    vector<int> cnt(4);
    for (int i = 0; i < n; ++i) {
      int tmp;
      cin >> tmp;
      ++cnt[tmp % p];
    }

    vector<vector<vector<vector<int>>>> dp(n + 1, vector<vector<vector<int>>>(n + 1, vector<vector<int>>(n + 1, vector<int>(4, -1))));
    dp[cnt[1]][cnt[2]][cnt[3]][0] = cnt[0];

    for (int i1 = n; i1 >= 0; --i1) {
      for (int i2 = n; i2 >= 0; --i2) {
        for (int i3 = n; i3 >= 0; --i3) {
          for (int rem = 0; rem < 4; ++rem) {
            if (i1 + i2 + i3 == 0)
              continue;
            if (dp[i1][i2][i3][rem] == -1)
              continue;

            int val = dp[i1][i2][i3][rem];
            if (rem == 0)
              ++val;

            if (i1 > 0) {
              int new_rem = (rem + 1) % p;
              dp[i1 - 1][i2][i3][new_rem] = max(dp[i1 - 1][i2][i3][new_rem], val);
            }

            if (i2 > 0) {
              int new_rem = (rem + 2) % p;
              dp[i1][i2 - 1][i3][new_rem] = max(dp[i1][i2 - 1][i3][new_rem], val);
            }

            if (i3 > 0) {
              int new_rem = (rem + 3) % p;
              dp[i1][i2][i3 - 1][new_rem] = max(dp[i1][i2][i3 - 1][new_rem], val);
            }
          }
        }
      }
    }

    int ans = 0;
    for (int rem = 0; rem < 4; ++rem)
      ans = max(ans, dp[0][0][0][rem]);

    cout << "Case #" << test << ": " << ans << endl;
  }


  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
