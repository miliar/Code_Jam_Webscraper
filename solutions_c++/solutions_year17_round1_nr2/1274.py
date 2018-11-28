#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef int Weight;

struct Edge {
  int src, dst;
  Edge(int src, int dst) :
    src(src), dst(dst) { }
};

bool operator < (const Edge &e, const Edge &f) {
  return e.src != f.src ? e.src < f.src : e.dst < f.dst;
}
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

typedef vector<Weight> Array;
typedef vector<Array> Matrix;

bool augment(const Graph& g, int u,
             vector<int>& matchTo, vector<bool>& visited) {
  if (u < 0) return true;
  FOR(e, g[u]) if (!visited[e->dst]) {
    visited[e->dst] = true;
    if (augment(g, matchTo[e->dst], matchTo, visited)) {
      matchTo[e->src] = e->dst;
      matchTo[e->dst] = e->src;
      return true;
    }
  }
  return false;
}

int bipartiteMatching(const Graph& g, int L, Edges& matching) {
  const int n = g.size();
  vector<int> matchTo(n, -1);
  int match = 0;
  REP(u, L) {
    vector<bool> visited(n);
    if (augment(g, u, matchTo, visited)) ++match;
  }
  REP(u, L) if (matchTo[u] >= 0) // make explicit matching
    matching.push_back( Edge(u, matchTo[u]) );
  return match;
}



int N, P;
int R[100];
int Q[100][100];

bool toolarge(int need, int here) {
  return need > here * 2;
}

bool isok(int need, int here) {
  int diff = abs(need - here);
  return diff * 10 <= need;
}

bool can2(int i, int j) {
  int fst = Q[0][i];
  int snd = Q[1][j];

  int n = 1;
  while (!toolarge(n * R[0], fst) and !toolarge(n * R[0], fst)) {
    if (isok(n * R[0], fst) && isok(n * R[1], snd))
      return true;
    ++n;
  }

  return false;
}

bool can1(int i) {
  int here = Q[0][i];

  int n = 1;
  while (!toolarge(n * R[0], here)) {
    if (isok(n * R[0], here))
      return true;
    ++n;
  }

  return false;
}

int f()
{
  scanf("%d%d", &N, &P);
  for (int i = 0; i < N; ++i)
    scanf("%d", &R[i]);
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < P; ++j)
      scanf("%d", &Q[i][j]);

  // printf("N=%d, P=%d", N, P);
  // for (int i = 0; i < N; ++i)
  //   printf(" %d", R[i]);
  // puts("");
  // for (int i = 0; i < N; ++i) {
  //   for (int j = 0; j < P; ++j)
  //     printf(" %d", Q[i][j]);
  //   puts("");
  // }

  int kit;

  if (N == 2) {
    Graph g;
    for (int i = 0; i < 2 * P; ++i)
      g.push_back(Edges());

    for (int i = 0; i < P; ++i)
      for (int j = 0; j < P; ++j)
        if (can2(i, j)) {
          g[i].push_back(Edge(i, P + j));
          g[P + j].push_back(Edge(P + j, i));
        }

    Edges matching;
    kit = bipartiteMatching(g, P, matching);
  } else if (N == 1) {
    kit = 0;
    for (int i = 0; i < P; ++i)
      if (can1(i)) ++kit;
  } else {
    assert(false);
  }

  return kit;
}

int main()
{
  freopen("B-small-attempt2.in", "r", stdin);
  freopen("B-small-attempt2.out", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int i=1; i<=T; ++i) {
    int y = f();
    printf("Case #%d: %d", i, y);
    puts("");
  }

  return 0;
}
