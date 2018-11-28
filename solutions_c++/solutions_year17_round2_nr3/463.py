#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
// head
const int N = 105;
const int M = 5e5;
const LL INF = 0x3f3f3f3f3f3f3f3fLL;

int l[N], s[N], t, n, q, u, v, cas = 1;
LL d[N][N];

void Floyd() {
  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }
//  for (int i = 1; i <= n; i++) {
//      for (int j = 1; j <= n; j++) {
//        printf("d[%d][%d]=%I64d\n", i, j, d[i][j]);
//      }
//    }
}

struct Graph {
	struct Edge {
		int to, nxt, v;
		Edge(int to, int nxt, int v) : to(to), nxt(nxt), v(v) {}
		Edge() {}
	};

	int head[N], ec;
	double dis[N];
	Edge e[M];

	void addEdge(int from, int to, int v) {
		e[ec] = Edge(to, head[from], v);
		head[from] = ec++;
	}
	void init(int n) {
		ec = 0;
		for (int i = 0; i <= n; i++) head[i] = -1;
	}
  double Dijkstra(int S, int T) {
    fill(dis, dis + n + 1, 1e100);
    dis[S] = 0;
    priority_queue<pair<double, int> > q;
    q.push({0.0, S});
    while (!q.empty()) {
      double dd = -q.top().fi;
      int cur = q.top().se;
      q.pop();
      if (dd > dis[cur]) continue;
      if (cur == T) return dis[T];
      for (int i = head[cur]; ~i; i = e[i].nxt) {
        int to = e[i].to;
        if (d[cur][to] <= l[cur] && dis[cur] + 1.0 * d[cur][to] / s[cur] < dis[to]) {
          dis[to] = dis[cur] + 1.0 * d[cur][to] / s[cur];
          q.push({-dis[to], to});
        }
      }
    }
    return dis[T];
  }
} g;


int main() {
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  while (t--) {
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++) {
      scanf("%d%d", l + i, s + i);
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        scanf("%I64d", d[i] + j);
        if (i == j) d[i][j] = 0;
        else if (d[i][j] == -1) d[i][j] = INF;
      }
    }
    Floyd();
    g.init(n);
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (i != j && d[i][j] != INF) {
          g.addEdge(i, j, 0);
        }
      }
    }
    printf("Case #%d: ", cas++);
    while (q--) {
      scanf("%d%d", &u, &v);
      printf("%.9f%c", g.Dijkstra(u, v), q == 0 ? '\n' : ' ');
    }
  }
  return 0;
}
