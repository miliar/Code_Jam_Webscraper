#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

const double PI = acos(-1);

int N, K;
LL r[2000000], h[2000000], a[2000000];
int p[2000];

bool cmp(int x, int y) {
  return a[x] < a[y];
}


int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", ++cas);
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i) {
      scanf("%lld%lld", &r[i], &h[i]);
      a[i] = r[i] * h[i];
      p[i] = i;
    }
    sort(p, p + N, cmp);
    LL mxA = 0;
    for (int i = 0; i < N; ++i) {
      LL A = r[p[i]] * r[p[i]] + 2 * r[p[i]] * h[p[i]];
      int cnt = 1;
      for (int j = N-1 ; j >= 0; --j) {
        if (j == i) continue;
        if (r[p[j]] > r[p[i]]) continue;
        if (cnt == K) break;
        A += 2 * r[p[j]] * h[p[j]];
        ++cnt;
      }
      if (A > mxA) mxA = A;
    }
    printf("%.9f\n", mxA * PI);
  }
  return 0;
}
