#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int n, q;
    cin >> n >> q;
    vector<vector<ll>> dist(n, vector<ll>(n));
    vi e(n), s(n);
    for (int i = 0; i < n; i++) {
      cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        cin >> dist[i][j];
        if (dist[i][j] == -1) {
          dist[i][j] = LLONG_MAX / 2;
        }
      }
    }
    for (int k = 0; k < n; k++) {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
    vector<long double> ans;
    while (q--) {
      int from, to;
      cin >> from >> to;
      from--; to--;
      vector<long double> cost(n, 1e100);
      vi done(n, false);
      cost[from] = 0;
      for (int iter = 1; iter < n; iter++) {
        int cur = -1;
        for (int i = 0; i < n; i++) {
          if (!done[i] && (cur == -1 || cost[i] < cost[cur])) {
            cur = i;
          }
        }
        if (cur == -1) {
          break;
        }
        done[cur] = 1;
        for (int next = 0; next < n; next++) {
          if (!done[next] && dist[cur][next] <= e[cur] && cost[next] > cost[cur] + 1.0l * dist[cur][next] / s[cur]) {
            cost[next] = cost[cur] + 1.0l * dist[cur][next] / s[cur];
          }
        }
      }
      ans.emplace_back(cost[to]);
    }
    static int caseNo = 1;
    printf("Case #%d:", caseNo++);
    for (auto x : ans) {
      printf(" %.6Lf", x);
    }
    puts("");
  }
  return 0;
}

