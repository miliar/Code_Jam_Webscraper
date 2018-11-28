#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
using namespace std;

long long e[110], s[110], d[110][110];
bool vis[110][110];

struct st {
  int city, horse;
  long long dist;
  st(int city, int horse, long long dist) : city(city), horse(horse), dist(dist) {}
  bool operator<(const st& o) const {
    if (city != o.city) return city < o.city;
    if (horse != o.horse) return horse < o.horse;
    return dist < o.dist;
  }
};

typedef pair<double, st> pdp;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, q; cin >> n >> q;
    for (int i = 0; i < n; i++)
      cin >> e[i] >> s[i];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        cin >> d[i][j];

    cout << "Case #" << c << ":";

    for (int i = 0; i < q; i++) {
      memset(vis, 0, sizeof(vis));
      int u, v; cin >> u >> v; u--; v--;
      double res;
      priority_queue<pdp, vector<pdp>, greater<pdp> > pq;
      pq.push(make_pair(0, st(u, u, 0)));
      while (!pq.empty()) {
        pdp top = pq.top(); pq.pop();
        st p = top.second;
        if (vis[p.city][p.horse]) continue;

        vis[p.city][p.horse] = true;

        // cout << top.first << " " << p.city << " " << p.horse << " " << p.dist << endl;

        if (p.city == v) {
          res = top.first;
          break;
        }

        for (int i = 0; i < n; i++) {
          if (i == p.city || d[p.city][i] == -1) continue;

          // same horse
          if (e[p.horse] >= p.dist + d[p.city][i] && !vis[i][p.horse]) {
            double ss = (1.0 * d[p.city][i]) / s[p.horse];
            pq.push(make_pair(top.first + ss, st(i, p.horse, p.dist + d[p.city][i])));
          }
        
          // new horse
          if (e[p.city] >= d[p.city][i] && !vis[i][p.city]) {
            double ss = (1.0 * d[p.city][i]) / s[p.city];
            pq.push(make_pair(top.first + ss, st(i, p.city, d[p.city][i])));
          }
        }
      }

      cout << " " << fixed << setprecision(8) << res;
    }
    cout << endl;
  }
  return 0;
}
