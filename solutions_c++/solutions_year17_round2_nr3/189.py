#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

const ll INF = numeric_limits<ll>::max() / 200;
ll es[105];
ll ss[105];
ll D[105][105];
ld dist[105];

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    ll n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
      cin >> es[i] >> ss[i];
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= n; j++) {
        ll d;
        cin >> d;
        D[i][j] = d == -1 ? INF : d;
      }

    for (int i = 1; i <= n; i++)
      D[i][i] = 0;
    for (int k = 1; k <= n; k++)
      for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
          if (D[i][k] + D[k][j] < D[i][j])
            D[i][j] = D[i][k] + D[k][j];

    cout << "Case #" << tt << ':';
    for (int qq = 0; qq < q; qq++) {
      fill(dist, dist + n + 1, INF);
      ll U, V;
      cin >> U >> V;
      priority_queue<pair<ld, ll>> q;
      dist[U] = 0;
      q.emplace(0, U);
      while (!q.empty()) {
        ld curd;
        ll curv;
        tie(curd, curv) = q.top();
        q.pop();
        curd = -curd;
        if (curd > dist[curv])
          continue;
        dist[curv] = curd;
        for (int next = 1; next <= n; next++)
          if (D[curv][next] <= es[curv] &&
              curd + ((ld)D[curv][next])/ss[curv] < dist[next]) {
            dist[next] = curd + ((ld)D[curv][next])/ss[curv];
            q.emplace(-dist[next], next);
          }
      }
      cout << ' ' << fixed << setprecision(10) << dist[V];
    }
    cout << '\n';
  }

  return 0;
}
