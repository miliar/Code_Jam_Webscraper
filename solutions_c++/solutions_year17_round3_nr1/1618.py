#include <bits/stdc++.h>

using namespace std;

struct Node {
  int x, y;
  bool operator < (const Node& C) const {
    return x < C.x;
  }
};
const int MAXN = 1005;
const double PI = acos(-1);
Node A[MAXN];
int T;
int K, N;
int Cas = 0;
double Max[MAXN];
int Vis[MAXN];
int main() {
  freopen("./in.txt", "r", stdin);
  freopen("./out.txt", "w", stdout);

  cin >> T;
  while(T--) {
    printf("Case #%d: ", ++Cas);
    scanf("%d%d", &N, &K);
    for(int i = 0; i < N; i++) {
      scanf("%d%d", &A[i].x, &A[i].y);
    }
    sort(A, A + N);
    memset(Max, 0, sizeof Max);
    memset(Vis, 0, sizeof Vis);
    double ans = 0;
    if(K == 1) ans = A[0].y * (double)A[0].x * 2.0 * PI + 
        A[0].x * (double) A[0].x * PI;
    Max[1] = A[0].y * PI * A[0].x * 2.0;
    Vis[1] = 1;
    for(int i = 1; i < N; i++) {
      if(Vis[K - 1]) ans = max(ans, Max[K - 1] + A[i].y * 
        (double) A[i].x * 2.0 * PI + A[i].x * (double) A[i].x * PI);
      if(K == 1) ans = max(A[i].y * (double)A[i].x * 2.0 * PI + 
          A[i].x * (double) A[i].x * PI, ans);
      for(int j = K - 1; j >= 2; j--) {
        if(Vis[j - 1]) {
          Max[j] = max(Max[j], Max[j - 1] + A[i].y * (double) A[i].x * 2.0 * PI);
          Vis[j] = 1;
        }
      }
      Max[1] = max(Max[1], A[i].y * (double) A[i].x * 2.0 * PI);
      //cout << ans << endl;
      //for(int j = 1; j <= K; j++) {
      //  cout << Max[j] << " ";
      //}
      //cout << endl;
    }
    printf("%.15f\n", ans);
  }
  return 0;
}
