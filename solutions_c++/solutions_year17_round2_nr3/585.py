#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const ll INF = 1.e16;

void fw(vector<vector<double>>& d) {
  int n = d.size();
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }
}
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n, q;
    cin >> n >> q;

    vector<ll> e(n), s(n);
    for (int i = 0; i < n; i++) cin >> e[i] >> s[i];

    vector<vector<double>> d(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        cin >> d[i][j];
        if (d[i][j] == -1) d[i][j] = INF;
      }
      d[i][i] = 0;
    }

    fw(d);

    vector<vector<double>> g(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (d[i][j] > e[i]) {
          g[i][j] = INF;
        } else {
          g[i][j] = d[i][j] / s[i];
        }
      }
    }

    fw(g);

    cout << "Case #" << tc << ':';
    for (int i = 0; i < q; i++) {
      int a, b;
      cin >> a >> b;
      a--; b--;
      cout << ' ' << fixed << setprecision(9) << g[a][b];
    }
    cout << '\n';
 }

}
