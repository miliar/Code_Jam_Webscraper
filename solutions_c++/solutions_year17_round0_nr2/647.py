#include <stdio.h>
#include <string>

long long fct(long long num, long long curr, long long mul) {
  if (num == 0) return curr;
  long long dig = num % 10LL;
  long long prev_dig = (num / 10LL) % 10LL;
  if (prev_dig <= dig) return fct(num / 10LL, curr, mul * 10LL);
  return fct(num * mul - 1ll, num * mul - 1ll, 1ll);

}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    char buff[32];
    long long N;
    scanf("%lld\n", &N);
    printf("Case #%d: %lld\n", t, fct(N, N, 1));
  }
}