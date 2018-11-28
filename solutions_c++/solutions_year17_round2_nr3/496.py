#include <iostream>
#include <vector>
using namespace std;

void solve() {
  int n, q;
  cin >> n >> q;
  vector<long long> e(n), s(n);
  vector<vector<long long>> d(n, vector<long long>(n));
  for (int i = 0; i < n; ++i) {
    cin >> e[i] >> s[i];
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cin >> d[i][j];
      if (d[i][j] == -1) {
        d[i][j] = 1e18;
      }
      d[i][i] = 0;
    }
  }
  auto dd = d;
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        dd[i][j] = min(dd[i][j], dd[i][k] + dd[k][j]);
      }
    }
  }
  vector<vector<double>> t(n, vector<double>(n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (dd[i][j] > e[i])
        t[i][j] = 1e18;
      else
        t[i][j] = static_cast<double>(dd[i][j]) / static_cast<double>(s[i]);
    }
  }
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
      }
    }
  }
  int u, v;
  for (int i = 0; i < q; ++i) {
    cin >> u >> v;
    u--, v--;
    cout << t[u][v] << ' ';
  }
}
int main() {
  cout.precision(20);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
