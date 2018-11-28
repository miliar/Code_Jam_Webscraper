#include <queue>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef long long ll;
typedef long long llint;
typedef pair<int, int> P;
#define X first
#define Y second

const int MAX = 205;

namespace Dinic {
  const int MAXV = 1000100;
  const int MAXE = 1000100;
  const llint oo = 1e18;

  int V, E;
  int last[MAXV], dist[MAXV], curr[MAXV];
  int next[MAXE], adj[MAXE]; llint cap[MAXE];

  void init(int n) {
    V = n;
    E = 0;
    REP(i, V) last[i] = -1;
  }

  void edge(int x, int y, llint c1, llint c2) {
    adj[E] = y; cap[E] = c1; next[E] = last[x]; last[x] = E++;
    adj[E] = x; cap[E] = c2; next[E] = last[y]; last[y] = E++;
  }

  llint push(int x, int sink, llint flow) {
    if (x == sink) return flow;

    for (int &e = curr[x]; e != -1; e = next[e]) {
      int y = adj[e];

      if (cap[e] && dist[x] + 1 == dist[y])
        if (llint f = push(y, sink, min(flow, cap[e])))
          return cap[e] -= f, cap[e^1] += f, f;
    }
    return 0;
  }

  llint run(int src, int sink) {
    llint ret = 0;
    for (;;) {
      REP(i, V) curr[i] = last[i];
      REP(i, V) dist[i] = -1;

      queue<int> Q;
      Q.push(src), dist[src] = 0;

      while (!Q.empty()) {
        int x = Q.front(); Q.pop();

        for (int e = last[x]; e != -1; e = next[e]) {
          int y = adj[e];
          if (cap[e] && dist[y] == -1) Q.push(y), dist[y] = dist[x] + 1;
        }
      }
      if (dist[sink] == -1) break;

      while (llint f = push(src, sink, oo)) ret += f;
    }
    return ret;
  }

  vector <P> reconstruct() {
    vector <P> R;

    REP(i, V)
      for (int e=last[i]; e != -1; e = next[e])
	if (!cap[e] && !(e % 2))
	  R.push_back(P(i, adj[e]));
      
    return R;
  }
}

int poc_norm[MAX][MAX], poc_dij[MAX][MAX];
int norm[MAX][MAX], dij[MAX][MAX];
int red[MAX], stup[MAX], dijpl[MAX], dijne[MAX];
int n, m;

llint solve_norm()
{
  Dinic::init(MAX*MAX);
  int S = 0, T = 1;
  int POLJE = 2;
  int RED = POLJE + n*n;
  int STUP = RED + n;

  REP(i, n) {
    if (!red[i]) Dinic::edge(S, RED + i, 1, 0);
    if (!stup[i]) Dinic::edge(STUP + i, T, 1, 0);
  }

  REP(i, n) REP(j, n) {
    Dinic::edge(RED + i, POLJE + i*n + j, 1, 0);
    Dinic::edge(POLJE + i*n + j, STUP + j, 1, 0);
  }
  
  llint kol = Dinic::run(S, T);
  auto V = Dinic::reconstruct();

  for (auto it : V)
    if (it.X >= POLJE && it.X < RED)
      norm[(it.X-POLJE)/n][(it.X-POLJE)%n] = 1;

  return kol;
}

llint solve_dij()
{
  Dinic::init(MAX*MAX);
  int S = 0, T = 1;
  int POLJE = 2;
  int DIJP = POLJE + n*n;
  int DIJN = DIJP + 2*n;

  REP(i, 2*n) {
    if (!dijpl[i]) Dinic::edge(S, DIJP + i, 1, 0);
    if (!dijne[i]) Dinic::edge(DIJN + i, T, 1, 0);
  }

  REP(i, n) REP(j, n) {
    Dinic::edge(DIJP + i + j, POLJE + i*n + j, 1, 0);
    Dinic::edge(POLJE + i*n + j, DIJN + i - j + n, 1, 0);
  }

  llint kol = Dinic::run(S, T);
  auto V = Dinic::reconstruct();

  for (auto it : V)
    if (it.X >= POLJE && it.X < DIJP)
      dij[(it.X-POLJE)/n][(it.X-POLJE)%n] = 1;

  return kol;
}

int main()
{
  int brt;
  scanf("%d", &brt);

  FOR(br, 1, brt+1) {
    scanf("%d%d", &n, &m);

    memset(norm, 0, sizeof norm);
    memset(dij, 0, sizeof dij);
    memset(red, 0, sizeof red);
    memset(stup, 0, sizeof stup);
    memset(dijpl, 0, sizeof dijpl);
    memset(dijne, 0, sizeof dijne);

    ll ret = 0;
    REP(i, m) {
      char c;
      int r, s;
      scanf(" %c%d%d", &c, &r, &s); r--; s--;
      if (c == '+' || c == 'o') {
	dij[r][s] = 1;
	dijpl[r+s] = 1;
	dijne[r-s+n] = 1;
	ret++;
      }
      if (c == 'x' || c == 'o') {
	norm[r][s] = 1;
	red[r] = 1;
	stup[s] = 1;
	ret++;
      }
    }

    memcpy(poc_norm, norm, sizeof norm);
    memcpy(poc_dij, dij, sizeof dij);
    
    ret += solve_norm() + solve_dij();    
    
    llint sum = 0;
    REP(i, n) REP(j, n) sum += norm[i][j] + dij[i][j];
    assert(sum == ret);

    vector <tuple<char, int, int> > R;
    
    REP(i, n) REP(j, n) {
      int prom = norm[i][j] + dij[i][j] - poc_norm[i][j] - poc_dij[i][j];
      if (!prom) continue;
      
      char c = 0;
      if (norm[i][j] && dij[i][j]) c = 'o';
      else if (norm[i][j]) c = 'x';
      else c = '+';

      R.push_back(make_tuple(c, i, j));
    }

    printf("Case #%d: %lld %d\n", br, ret, (int) R.size());
    for (auto it : R)
      printf("%c %d %d\n", get<0>(it), get<1>(it) + 1, get<2>(it) + 1);
  }
  
  return 0;
}
