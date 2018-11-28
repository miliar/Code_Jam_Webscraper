#include <bits/stdc++.h>

using namespace std;

#define SMALL
//#define LARGE

const int INF = 0x7f7f7f7f;
const int N = 20005;
const int M = 4000005;

struct Edge {
  int u, v, c, nxt;
  
  Edge() {}
  Edge(const int& _u, const int& _v, const int& _c, const int& _nxt) : u(_u), v(_v), c(_c), nxt(_nxt) {}
} es[M];

int head[N], cur[N], depth[N], tot;

void addEdge(const int& u, const int& v, const int& c) {
  es[tot] = Edge(u, v, c, head[u]);
  head[u] = tot++;
}

bool bfs(const int& s, const int& t) {
  deque <int> de;
  de.push_back(s);
  memset(depth, 0x7f, sizeof(depth));
  depth[s] = 0;
  while (!de.empty()) {
    int u = de.front();
    de.pop_front();
    for (int i = head[u]; i != -1; i = es[i].nxt) {
      int v = es[i].v;
      if (es[i].c > 0 && depth[v] == INF)
        depth[v] = depth[u] + 1, de.push_back(v);
    }
  }
  return depth[t] != INF;
}

int dfs(const int& u, const int& t, const int& now) {
  if (u == t)
    return now;
  int flow = 0;
  for (int &i = cur[u]; i != -1; i = es[i].nxt) {
    int v = es[i].v;
    if (depth[u] + 1 != depth[v] || es[i].c == 0)
      continue;
    int temp = dfs(v, t, min(now - flow, es[i].c));
    es[i].c -= temp;
    es[i ^ 1].c += temp;
    flow += temp;
    if (flow == now)
      break;
  }
  if (!flow)
    depth[u] = INF;
  return flow;
}

int dinic(const int& s, const int& t) {
  int ret = 0;
  while (bfs(s, t)) {
    memcpy(cur, head, sizeof(cur));
    ret += dfs(s, t, INF);
  }
  return ret;
}

int n, c, m;
int u[N], v[N], s[N][N], t[N];
int ans1, ans2;

int getMaxFlow(const int& r, const int& ch) {
  memset(head, -1, sizeof(head));
  tot = 0;
  for (int i = 1; i <= n; ++i) {
    addEdge(0, i, r);
    addEdge(i, 0, 0);
  }
  for (int i = 1; i <= c; ++i) {
    addEdge(n + i, n + c + 1, r);
    addEdge(n + c + 1, n + i, 0);
  }
  for (int i = 1; i < n; ++i) {
    addEdge(i, i + 1, ch);
    addEdge(i + 1, i, 0);
  }
  for (int i = 1; i <= c; ++i) {
    for (int j = n; j > 0; --j) {
      if (s[i][j] == 0)
        continue;
      addEdge(j, i + n, s[i][j]);
      addEdge(i + n, j, 0);
    }
  }
  return dinic(0, n + c + 1);
}

int isAns(const int& ride) {
  int bot = 0, top = 1001;
  while (bot < top) {
    int mid = (bot + top) >> 1;
    if (getMaxFlow(ride, mid) == m)
      top = mid;
    else
      bot = mid + 1;
  }
  return top;
}

void getAns() {
  int bot = 1, top = 1000;
  while (bot < top) {
    int mid = (bot + top) >> 1;
    int temp = isAns(mid);
    if (temp <= 1000)
      top = mid;
    else
      bot = mid + 1;
  }
  ans1 = bot; ans2 = isAns(ans1);
}

int main()
{
#ifdef SMALL
  freopen("B-small.in", "r", stdin);
  freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  for (int Case = 1; Case <= T; ++Case) {
    memset(t, 0, sizeof(t));
    memset(s, 0, sizeof(s));
    scanf("%d %d %d", &n, &c, &m);
    for (int i = 0; i < m; ++i) {
      scanf("%d %d", &u[i], &v[i]);
      ++s[v[i]][u[i]];
      ++t[v[i]];
    }
    getAns();
    printf("Case #%d: %d %d\n", Case, ans1, ans2);
    fprintf(stderr, "Case %d finished\n", Case);
  }
  return 0;
}
