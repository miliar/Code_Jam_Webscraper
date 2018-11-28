#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const double EPS = 1e-8;
const int MX = 1010;
int T, C = 1;
int D, N, S[MX], K[MX];

int main() {
	freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", C++);
    scanf("%d %d", &D, &N);
    for(int i = 1; i <= N; i++) {
      scanf("%d %d", &K[i], &S[i]);
    }
    double max_t = (1.0 * D - K[N]) / S[N];
    for(int i = N - 1; i >= 1; --i) {
      double my_t = (1.0 * D - K[i]) / S[i];
      if(my_t <= max_t) continue;
      else {
        max_t = my_t;
      }
    }
    double ans = (1.0 * D) / max_t;
    printf("%.6lf\n", ans);
  }
}
