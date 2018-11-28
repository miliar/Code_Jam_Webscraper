#include <assert.h>
#include <iostream>

using namespace std;

typedef long long ll;

const int N = 105;
int n, m;
ll max_dist[N], speed[N];
ll dist[N][N];
ll cum_dist[N];

bool viz[N][N];
double dp[N][N];

double solve(int u, int horse) {
  if (u == n - 1) {
    return 0;
  }

  double &d = dp[u][horse];
  if (viz[u][horse]) {
    return d;
  }

  ll dist_expended = cum_dist[u] - cum_dist[horse];
  ll remain_dist = max_dist[horse] - dist_expended;
  assert(remain_dist >= 0);

  double ret = -1;
  if (remain_dist >= dist[u][u + 1]) {
    double t = solve(u + 1, horse);
    double nt = t + 1.0 * dist[u][u + 1] / speed[horse];
    if (ret == -1) {
      ret = nt;
    } else {
      ret = min(ret, nt);
    }
  }

  if (max_dist[u] >= dist[u][u + 1]) {
    double t = solve(u + 1, u);
    double nt = t + 1.0 * dist[u][u + 1] / speed[u];
    if (ret == -1) {
      ret = nt;
    } else {
      ret = min(ret, nt);
    }
  }

  viz[u][horse] = true;
  return d = ret;
}

int main() {
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      cin >> max_dist[i] >> speed[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> dist[i][j];
      }
    }
    int start, end;
    cin >> start >> end;
    start--; end--;
    assert(start == 0);
    assert(end == n - 1);
    cum_dist[0] = 0;
    for (int i = 1; i < n; ++i) {
      cum_dist[i] = cum_dist[i - 1] + dist[i - 1][i];
    }
    memset(viz, 0, sizeof(viz));
    printf("Case #%d: %.7lf\n", t + 1, solve(start, 0));
  }
}
