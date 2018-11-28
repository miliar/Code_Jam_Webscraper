#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

//typedef pair<int, int> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

struct edge {
  edge(int t, int c, int r) : to(t), cap(c), rev(r) {}
  int to, cap, rev;
};

int T;
int N, P, V;
int W[50];
int L[50][50], R[50][50];
vector<edge> G[3000];
bool used[3000];

int mp(int n, int x) {
  return 1 + n*P + x;
}
void add_edge(int s, int t) {
  G[s].pb(edge(t, 1, G[t].size()));
  G[t].pb(edge(s, 0, G[s].size()-1));
}

int dfs(int v, int p, int f) {
  if (v == p) return f;
  used[v] = true;
  for (auto &e : G[v]) {
    if (!used[e.to] && e.cap > 0) {
      int d = dfs(e.to, p, min(f, e.cap));
      if (d > 0) {
        e.cap -= d;
        G[e.to][e.rev].cap += d;
        return d;
      }
    }
  }
  return 0;
}

int max_flow(int s, int t) {
  int flow = 0;
  while (true) {
    rep(i, V) used[i] = false;
    int f = dfs(s, t, INF);
    if (f == 0) return flow;
    flow += f;
  }
}

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, T) {
    cin >> N >> P;
    rep(i, N) cin >> W[i];
    rep(i, N) {
      rep(j, P) {
        int x;
        cin >> x;
        L[i][j] = (x*10 + W[i]*11-1) / (W[i]*11);
        R[i][j] = (x*10) / (W[i]*9);
      }
    }
    V = 2 + N*P;
    rep(i, V) G[i].clear();
    rep(i, P) {
      if (L[0][i] > R[0][i]) continue;
      add_edge(0, mp(0, i));
    }
    for (int i=1; i<N; i++) {
      rep(a, P) {
        rep(b, P) {
          if (L[i-1][a] > R[i-1][a] || L[i][b] > R[i][b]) continue;
          //if ((R[i-1][a] > L[i][b]) && (R[i][b] > L[i-1][a])) continue;
          if ((L[i-1][a] >= L[i][b] && L[i-1][a] <= R[i][b]) ||
              (L[i][b] >= L[i-1][a] && L[i][b] <= R[i-1][a])) {
            add_edge(mp(i-1, a), mp(i, b));
          }
        }
      }
    }
    rep(i, P) {
      if (L[N-1][i] > R[N-1][i]) continue;
      add_edge(mp(N-1, i), V-1);
    }
    cout << "Case #" << i+1 << ": " << max_flow(0, V-1) << "\n";
  }
  return 0;
}
