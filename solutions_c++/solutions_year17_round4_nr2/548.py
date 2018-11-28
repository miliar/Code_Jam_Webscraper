#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    int n, c, m;
    cin >> n >> c >> m;

    vector<int> client(c), seat(n), sum_col(n), sum(n);
    int board[c][n];
    memset(board, 0, sizeof board);

    for (int i = 0; i < m; ++i) {
      int pi, ci;
      cin >> pi >> ci;
      pi--; ci--;

      seat[pi]++;
      client[ci]++;
      board[ci][pi]++;
    }

    for (int i = 0; i < c; ++i) {
      for (int j = 0; j < n; ++j) {
        sum_col[j] += board[i][j];
      }
    }

    sum[0] = sum_col[0];
    for (int j = 1; j < n; ++j) {
      sum[j] = sum[j - 1] + sum_col[j];
    }

    int ticket_client = *max_element(client.begin(), client.end());
    int lo = max(ticket_client, (m + n - 1) / n);
    lo = max(lo, seat[0]) - 1;

    int hi = m;

    while (hi - lo > 1) {
      int x = (lo + hi) / 2;
      bool is_valid = true;

      for (int pos = 0; pos < n; ++pos) {
        if ((pos + 1) * x < sum[pos]) {
          is_valid = false;
          break;
        }
      }

      if (is_valid) {
        hi = x;
      } else {
        lo = x;
      }
    }

    int y = hi;
    int z = 0;
    for (int pos = 0; pos < n; ++pos) {
      z += max(0, sum_col[pos] - y);
    }

    cout << y << " " << z << endl;
  }

  return 0;
}
