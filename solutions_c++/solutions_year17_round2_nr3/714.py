#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
const long long MAX = 0x3fffffff;
int T;
int N, Q;
vector<int> E, S;
long long tab[101][101];
double ttab[101][101];
pair<int, int> query[101];
int main() {
  scanf("%d\n", &T);
  for (int TT = 1; TT <= T; TT++) {
    scanf("%d%d", &N, &Q);
    E.resize(N + 1);
    S.resize(N + 1);
    for (int i = 1; i <= N; i++) {
      scanf("%d%d", &E[i], &S[i]);
    }
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        scanf("%lld", &tab[i][j]);
        if (tab[i][j] == -1)
          tab[i][j] = MAX * MAX;
      }
    }
    for (int i = 0; i < Q; i++) {
      scanf("%d%d", &query[i].first, &query[i].second);
    }
    //D f
    for (int k = 1; k <= N; k++)
      for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
          tab[i][j] = min(tab[i][j], tab[i][k] + tab[k][j]);
    //TT
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= N; j++)
        if (tab[i][j] <= E[i])
          ttab[i][j] = tab[i][j] / double(S[i]);
        else
          ttab[i][j] = double(MAX) * MAX;
    //TF
    for (int k = 1; k <= N; k++)
      for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
          ttab[i][j] = min(ttab[i][j], ttab[i][k] + ttab[k][j]);

    printf("Case #%d:", TT);
    for (int i=0;i<Q;i++)
      printf(" %.8lf", ttab[query[i].first][query[i].second]);
    printf("\n");
  }
  return 0;
}
