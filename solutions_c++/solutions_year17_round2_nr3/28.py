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
typedef pair<int, int> P;
#define X first
#define Y second

const int MAX = 105;
const ll INF = 1e18;

ll prevali[MAX], brz[MAX];
int e[MAX][MAX];
ll dist[MAX][MAX];
double sol[MAX][MAX];
int n;

void floyd_1() {
  REP(i, MAX) REP(j, MAX) dist[i][j] = INF;
  REP(i, MAX) dist[i][i] = 0;
  REP(i, MAX) REP(j, MAX)
    if (e[i][j] != -1) dist[i][j] = e[i][j];

  REP(i, n) REP(j, n) REP(k, n)
    dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k]);
}

void floyd_2() {
  REP(i, MAX) REP(j, MAX) sol[i][j] = INF;
  REP(i, MAX) sol[i][i] = 0;
  REP(i, MAX) REP(j, MAX)
    if (dist[i][j] <= prevali[i])
      sol[i][j] = min(sol[i][j], (double) dist[i][j] / (double) brz[i]);

  REP(i, n) REP(j, n) REP(k, n)
    sol[j][k] = min(sol[j][k], sol[j][i] + sol[i][k]);
}

int main()
{
  int brt;
  scanf("%d", &brt);

  REP(tt, brt) {
    int q;
    scanf("%d%d", &n, &q);

    REP(i, n) scanf("%lld%lld", &prevali[i], &brz[i]);
    REP(i, n) REP(j, n) scanf("%d", &e[i][j]);
    floyd_1();
    floyd_2();

    printf("Case #%d: ", tt+1);

    REP(i, q) {
      int a, b;
      scanf("%d%d", &a, &b); a--; b--;
      assert(sol[a][b] < INF/2);
      printf("%.10lf ", sol[a][b]);
    }
    printf("\n");    
  }

  return 0;
}
