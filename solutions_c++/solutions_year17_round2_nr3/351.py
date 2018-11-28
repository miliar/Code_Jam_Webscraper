#include <iostream>
#include <queue>
#include <string.h>
#include <iomanip>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(9);
  int T, n, q;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> n >> q;
    int e[n+1], s[n+1];
    long long d[n+1][n+1];
    for (int i=1; i<=n; i++) cin >> e[i] >> s[i];
    for (int i=1; i<=n; i++)
      for (int j=1; j<=n; j++)
        cin >> d[i][j];
    for (int i=1; i<=n; i++)
      for (int j=1; j<=n; j++)
        for (int k=1; k<=n; k++)
          if (d[j][i] != -1 && d[i][k] != -1)
            if (d[j][k] == -1 || d[j][k] > d[j][i] + d[i][k])
              d[j][k] = d[j][i] + d[i][k];
    int u, v;
    bool vis[n+1];
    cout << "Case #" << t << ": ";
    for (int i=0; i<q; i++) {
      cin >> u >> v;
      priority_queue<pair<double, int>> q;
      q.push({0.0, u});
      memset(vis, 0, (n+1)*sizeof(int));
      double res = 0;
      while (!q.empty()) {
        pair<double, int> p = q.top();
        int x = p.second;
        double dist = -p.first;
        if (x == v) {
          res = dist;
          break;
        }
        q.pop();
        if (vis[x]) continue;
        vis[x] = true;
        for (int i=1; i<=n; i++)
          if (d[x][i] != -1 && d[x][i] <= e[x])
            q.push({-(dist + 1.0 * d[x][i] / s[x]), i});
      }
      cout << res << " ";
    }
    cout << "\n";
  }
  return 0;
}
