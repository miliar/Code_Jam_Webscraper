#include <bits/stdc++.h>

using namespace std;

const int N = 110;

int n, q;
int e[N], s[N];
int d[N][N];
int vis[N][N];
double dis[N][N];

struct node {
  double d;
  int u;
  int hr;
  int l;
  bool operator<(const node & x) const {
    return d < x.d;
  }
};

void fillinit() {
  for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) dis[i][j] = 1e20;
  memset(vis, 0, sizeof(vis));
}

double go(int x, int y) {
  fillinit();
  dis[x][x] = 0;
  priority_queue<node> q;
  double ret = 1e20;
  q.push({0, x, x, 0});
  while (!q.empty()) {
    auto t = q.top();
    q.pop();
    if (vis[t.u][t.hr]) continue;
    vis[t.u][t.hr] = 1;
    if (t.u == y) ret = min(ret, dis[t.u][t.hr]);
    for (int i = 1; i <= n; ++i) {
      if (d[t.u][i] != -1) {
        if (e[t.u] >= d[t.u][i]) {
          double tmp = (double)d[t.u][i] / s[t.u] + dis[t.u][t.hr];
          if (dis[i][t.u] > tmp) {
            dis[i][t.u] = tmp;
            q.push({-tmp, i, t.u, d[t.u][i]});
          }
        }
        if (d[t.u][i] + t.l <= e[t.hr]) {
          double tmp = (double)d[t.u][i] / s[t.hr] + dis[t.u][t.hr];
          if (dis[i][t.hr] > tmp) {
            dis[i][t.hr] = tmp;
            q.push({-tmp, i, t.hr, d[t.u][i] + t.l});
          }
        }
      }
    }
  }
  return ret;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; ++i) {
      scanf("%d%d", e + i, s + i);
    }
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        scanf("%d", d[i] + j);
      }
    }
    double ans[N];
    for (int i = 1, x, y; i <= q; ++i) {
      scanf("%d%d", &x, &y);
      ans[i] = go(x, y);
    }
    printf("Case #%d:", _);
    for (int i = 1; i <= q; ++i) printf(" %.8f", ans[i]);
    puts("");
  }
  return 0;
}
