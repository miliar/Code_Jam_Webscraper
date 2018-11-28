#include <algorithm>
#include <array>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void solve() {
  typedef long long ll;
  const ll oo = numeric_limits<ll>::max() / 2;
  ll n, q;
  cin >> n >> q;
  vector<ll> e(n), s(n);
  vector<vector<ll>> m(n, vector<ll>(n));
  for (int i = 0; i < n; i++) {
    cin >> e[i] >> s[i];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> m[i][j];
      if (m[i][j] == -1) {
        m[i][j] = oo;
      }
      if (i == j) {
        m[i][j] = 0;
      }
    }
  }
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        m[i][j] = min(m[i][j], m[i][k] + m[k][j]);
      }
    }
  }
  vector<vector<double>> M(n, vector<double>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      M[i][j] = oo;
      if (m[i][j] <= e[i]) {
        M[i][j] = (double)m[i][j] / s[i];
      }
    }
  }
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        M[i][j] = min(M[i][j], M[i][k] + M[k][j]);
      }
    }
  }
  for (int i = 0; i < q; i++) {
    int u, v;
    cin >> u >> v;
    printf(" %.10f", M[u - 1][v - 1]);
  }
  puts("");
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":";
    solve();
  }
}
