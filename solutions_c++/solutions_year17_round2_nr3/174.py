#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int N, Q;
int E[101], S[101], G[101][101], U[101], V[101];
double ans[101];

void dijkstra(int s) {
  typedef tuple<int, int, int> iii; // i S E
  typedef tuple<double, int, int, int> iiii; // dist i S E;
  priority_queue<iiii, vector<iiii>, greater<iiii>> pq;

  set<int> want;
  REP (i, Q) if (U[i] == s) want.insert(V[i]);

  map<int, double> mindist;
  map<iii, double> dist;
  dist[iii(s, 1, -1)] = 0.0;
  pq.emplace(0.0, s, 1, -1);
  while (!pq.empty()) {
    double cd;
    int cu, cs, ce;
    tie(cd, cu, cs, ce) = pq.top(); pq.pop();

    if (mindist.find(cu) == mindist.end() ||
        mindist[cu] > cd)
      mindist[cu] = cd;

    want.erase(cu);
    if (want.empty()) break;

    if (cd > dist[iii(cu, cs, ce)]) continue;
    REP (nu, N) if (G[cu][nu] != -1) {
      int ns, ne; double nd;
      if (G[cu][nu] <= ce) {
        // can use this horse
        nd = cd + (double) G[cu][nu] / cs;
        ne = ce - G[cu][nu];
        ns = cs;
        if (dist.find(iii(nu, ns, ne)) == dist.end() ||
            dist[iii(nu, ns, ne)] > nd) {
          dist[iii(nu, ns, ne)] = nd;
          pq.emplace(nd, nu, ns, ne);
        }
      }
      if (G[cu][nu] <= E[cu]) {
        // can use horse at this vertex
        nd = cd + (double) G[cu][nu] / S[cu];
        ne = E[cu] - G[cu][nu];
        ns = S[cu];
        if (dist.find(iii(nu, ns, ne)) == dist.end() ||
            dist[iii(nu, ns, ne)] > nd) {
          dist[iii(nu, ns, ne)] = nd;
          pq.emplace(nd, nu, ns, ne);
        }
      }
    }
  }

  REP (i, Q) if (U[i] == s) {
    ans[i] = mindist[V[i]];
  }
}

int main() {
  int T;
  cin >> T;
  REP (tc, T) {
    cin >> N >> Q;
    REP (i, N) cin >> E[i] >> S[i];
    REP (i, N) REP (j, N) cin >> G[i][j];
    REP (i, Q) {
      ans[i] = -1;
      cin >> U[i] >> V[i];
    }

    REP (i, Q) if (ans[i] < 0) {
      dijkstra(U[i]);
    }

    cout << "Case #" << tc << ":";
    REP (i, Q) cout << " " << fixed << setprecision(9) << ans[i];
    cout << endl;
  }
  return 0;
}
