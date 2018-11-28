#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-7
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define bits(a) __builtin_popcount(a)

using namespace std;

char s[105][105];
char _s[105][105];
bool s1[105][105];
bool s2[105][105];

const int MAXN = 406;

struct edge {
    int a, b, cap, flow;
};

struct Dinic
{
  int n, d[MAXN], ptr[MAXN], q[MAXN];
  vector<edge> e;
  vector<int> g[MAXN];

  Dinic(int N) : n(N) {}

  void AddEdge(int a, int b, int cap)
  {
    edge e1 = {a, b, cap, 0};
    edge e2 = {b, a, 0, 0};
    g[a].pb((int) e.size());
    e.pb(e1);
    g[b].pb((int) e.size());
    e.pb(e2);
  }

  bool bfs(int s, int t)
  {
    int qh = 0, qt = 0;
    q[qt++] = s;
    memset (d, -1, n * sizeof d[0]);
    d[s] = 0;
    while(qh < qt && d[t] == -1)
    {
      int v = q[qh++];
      for(size_t i=0; i<g[v].size(); ++i)
      {
        int id = g[v][i], to = e[id].b;
        if(d[to] == -1 && e[id].flow < e[id].cap)
        {
          q[qt++] = to;
          d[to] = d[v] + 1;
        }
      }
    }
    return d[t] != -1;
  }

  int dfs(int v, int flow, int t)
  {
    if(!flow) return 0;
    if(v == t) return flow;
    for(;ptr[v]<(int)g[v].size();++ptr[v])
    {
      int id = g[v][ptr[v]], to = e[id].b;
      if(d[to] != d[v] + 1) continue;
      int pushed = dfs(to, min(flow, e[id].cap - e[id].flow), t);
      if(pushed)
      {
        e[id].flow += pushed;
        e[id^1].flow -= pushed;
        return pushed;
      }
    }
    return 0;
  }

  int GetMaxFlow(int s, int t)
  {
    int flow = 0;
    while(bfs(s, t))
    {
      memset(ptr, 0, n * sizeof ptr[0]);
      while(int pushed = dfs(s, INF, t))
        flow += pushed;
    }
    return flow;
  }
};

void solve1(int n)
{
  if(n == 1)
  {
    s1[0][0] = true;
    return;
  }
  bool ldiag[2*n], rdiag[2*n];
  setzero(ldiag);
  setzero(rdiag);
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
    {
      if(s1[i][j])
      {
        ldiag[i + j] = true;
        rdiag[i - j + n] = true;
      }
    }
  Dinic solver(4 * n + 5);
  int s = 4*n, t = 4*n + 1;
  for(int d=0;d<2*n-1;d++)
    if(!ldiag[d])
      solver.AddEdge(s, d, 1);
  for(int d=0;d<2*n-1;d++)
    if(!rdiag[d])
      solver.AddEdge(d + 2*n, t, 1);
  for(int d=0;d<2*n-1;d++)
  {
    if(ldiag[d]) continue;
    for(int i=0;i<=min(d, n - 1);i++)
    {
      int j = d - i;
      if(j >= n || rdiag[i - j + n]) continue;
      solver.AddEdge(d, i - j + 3*n, 1);
    }
  }
  solver.GetMaxFlow(s, t);
  for(int d=0;d<2*n-1;d++)
  {
    if(ldiag[d]) continue;
    for(int x : solver.g[d])
    {
      edge e = solver.e[x];
      if(e.b == s || e.flow != 1) continue;
      int dd = e.b;
      int i = (d + dd - 3*n) / 2;
      int j = d - i;
      assert(i < n && i >= 0 && j < n && j >= 0 && !s1[i][j]);
      s1[i][j] = true;
    }
  }
}

void solve2(int n)
{
  bool row[n], col[n];
  setzero(row);
  setzero(col);
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
    {
      if(s2[i][j])
      {
        row[i] = true;
        col[j] = true;
      }
    }
  for(int i=0;i<n;i++)
  {
    if(row[i]) continue;
    for(int j=0;j<n;j++)
    {
      if(col[j]) continue;
      s2[i][j] = true;
      col[j] = true;
      break;
    }
  }
}

int main()
{
  freopen("D-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int n, m, x, y;
    char c;
    scanf("%d %d", &n, &m);
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
      {
        s[i][j] = '.';
        s1[i][j] = false;
        s2[i][j] = false;
      }
    for(int i=0;i<m;i++)
    {
      scanf(" %c %d %d", &c, &x, &y);
      s[x-1][y-1] = c;
      if(c != 'x') s1[x-1][y-1] = true;
      if(c != '+') s2[x-1][y-1] = true;
    }
    solve1(n);
    solve2(n);
    int ans = 0;
    vector<pair<char, pair<int, int> > > v;
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
      {
        if(s1[i][j] && s2[i][j]) _s[i][j] = 'o', ans += 2;
        else if(s1[i][j]) _s[i][j] = '+', ans++;
        else if(s2[i][j]) _s[i][j] = 'x', ans++;
        else _s[i][j] = '.';
        if(s[i][j] != _s[i][j])
        {
          assert(s[i][j] == '.' || _s[i][j] == 'o');
          v.pb(mp(_s[i][j], mp(i + 1, j + 1)));
        }
      }
    printf("Case #%d: %d %d\n", tt++, ans, v.size());
    for(auto p : v)
      printf("%c %d %d\n", p.f, p.s.f, p.s.s);
  }
  return 0;
}
