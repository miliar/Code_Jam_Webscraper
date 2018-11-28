#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

#define INF (123456789000LL)

using namespace std;

int T, N, Q, x, y;

int main(void) {
  cin >> T;
  REP(t, T) {
    cin >> N >> Q;
    vector<vector<long long> > D(N, vector<long long>(N));
    vector<int> E(N);
    vector<int> S(N);
    vector<vector<long long> > dist(N, vector<long long>(N, INF));
    vector<vector<long double> > G(N, vector<long double>(N, INF));
    REP(n, N) {
      cin >> E[n] >> S[n];
    }
    REP(i, N) {
      REP(j, N) {
        cin >> D[i][j];
        if (D[i][j] > -1) dist[i][j] = D[i][j];
      }
    }
    REP(k, N) REP(i, N) REP(j, N) dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
    REP(i, N) G[i][i] = 0;
    REP(i, N) REP(j, N) {
      if (E[i] < dist[i][j]) continue;
      G[i][j] = (long double)dist[i][j] / (long double)S[i];
    }
    REP(k, N) REP(i, N) REP(j, N) G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
    printf("Case #%d: ", t+1);
    REP(q, Q) {
      cin >> x >> y;
      printf("%.10Lf", G[x-1][y-1]);
      if (q < Q-1) printf(" ");
      else printf("\n");

    }
  }
  return 0;
}
