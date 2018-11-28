#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long LL;

LL K, N, ans;
LL a[2000000], an = 0;

void solve(LL n) {
  if (n == 0) return;
  a[an++] = n;
  solve(n/2);
  solve((n-1)/2);
}

int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    an = 0;
    printf("Case #%d: ", ++cas);
    scanf("%lld%lld", &N, &K);
    solve(N);
    sort(a, a+an);
    if (a[N-K] % 2 != 0) {
      printf("%lld %lld\n", (a[an-K]-1)/2, (a[an-K]-1)/2);
    } else {
      printf("%lld %lld\n", a[an-K]/2, (a[an-K]-1)/2);
    }
  }
  return 0;
}
