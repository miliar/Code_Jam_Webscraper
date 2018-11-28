#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug
//#define TRACE(x)

using namespace std;

typedef long long llint;

const int MAXN = 110;
const double INF = 1e15;

int n, q, e[MAXN], s[MAXN], ptr;
double d[MAXN][MAXN];
double f[MAXN][MAXN];

inline double get(int x, int z) {
  if (d[x][z] == INF) return INF;
  if (d[x][z] > e[x]) return INF;
  return d[x][z] / (double)s[x];
}

struct cmpf {
  bool operator()(const int &i, const int &j) {
    if (f[i][ptr] != f[j][ptr]) return f[i][ptr] < f[j][ptr];
    return i < j;
  }
};

set<int, cmpf> st;

void solve(int tc) {
  scanf("%d %d",&n,&q);
  REP(i, n) scanf("%d %d",&e[i],&s[i]);
  REP(i, n) REP(j, n) {
    scanf("%lf",&d[i][j]);
    if (d[i][j] == -1)
      d[i][j] = INF;
    if (i == j)
      d[i][j] = 0;
  }

  REP(k, n) REP(i, n) REP(j, n)
    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

  REP(y, n) {
    REP(x, n) f[x][y] = INF;
    ptr = y;
    f[y][y] = 0;
    st.insert(y);

    while (!st.empty()) {
      int z = *st.begin();
      st.erase(st.begin());

      REP(x, n)
	if (f[x][y] > get(x, z) + f[z][y]) {
	  st.erase(x);
	  f[x][y] = get(x, z) + f[z][y];
	  st.insert(x);
	}
    }
  }
  
  printf("Case #%d: ",tc);
  
  REP(i, q) {
    int u, v;
    scanf("%d %d",&u,&v);
    --u;
    --v;
    printf("%.8lf ",f[u][v]);
  }
  printf("\n");
}

int main(void) {
  int tc;
  scanf("%d",&tc);
  REP(it, tc) {
    solve(it+1);
  }
  return 0;
}
