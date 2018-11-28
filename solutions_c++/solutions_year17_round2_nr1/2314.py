#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long int lld;

int main() {
  int t, n;
  lld d, ki, si;
  double tt;
  scanf("%d", &t);
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%lld %d", &d, &n);
    tt = 0.0;
    for(int i = 0; i < n; ++i) {
      scanf("%lld %lld", &ki, &si);
      tt = max(tt, ((double)d - ki)/si);
    }
    printf("Case #%d: %.6lf\n", cas, d/tt);
  }
}