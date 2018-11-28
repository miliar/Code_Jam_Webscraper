#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

double min(double x, double y) { return x < y ? x : y; }

LL D, N;

int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", ++cas);
    scanf("%lld%lld", &D, &N);
    double t = 0;
    for (int i = 0; i < N; ++i) {
      LL K, S;
      scanf("%lld%lld", &K, &S);
      double tmp = ((D - K) * 1.0)/S;
      if (tmp > t + 1e-9) {
        t = tmp;
      }
    }
    printf("%6f\n", (D * 1.0)/t);
  }
  return 0;
}
