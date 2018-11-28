#include <stdio.h>
#include <cassert>

const long long INF = 1e15;

long long E[101], D[101][101], dis[101][101];
double S[101], time[101][101];

void dijkstra(int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (D[i][j] == -1) dis[i][j] = INF;
      else dis[i][j] = D[i][j];
    }
  }
  for (int k = 0; k < n; ++k)
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        if (dis[i][k] + dis[k][j] < dis[i][j])
          dis[i][j] = dis[i][k] + dis[k][j];
}

void run(int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (dis[i][j] <= E[i]) time[i][j] = dis[i][j] / S[i];
      else time[i][j] = INF;
    }
  }
  for (int k = 0; k < n; ++k)
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        if (time[i][k] + time[k][j] < time[i][j])
          time[i][j] = time[i][k] + time[k][j];
}

int main() {
  int T, N, Q, a, b;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d", &N, &Q);
    for (int i = 0; i < N; ++i)
      scanf("%lld%lf", &E[i], &S[i]);
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j)
        scanf("%lld", &D[i][j]);
    dijkstra(N);
    run(N);
    printf("Case #%d:", t);
    for (int i = 0; i < Q; ++i) {
      scanf("%d%d", &a, &b);
      assert(time[a-1][b-1] < INF);
      printf(" %lf", time[a-1][b-1]);
    }
    printf("\n");
  }
  return 0;
}
