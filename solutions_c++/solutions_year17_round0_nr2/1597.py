#include <cstdio>
#include <algorithm>

typedef unsigned long long u64;

const int N = 20;

int tot, a[N], b[N];

u64 calc() {
  u64 res = 0;
  for (int i = tot; i > 0; --i) res = 10 * res + b[i];
  return res;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    u64 n;
    scanf("%llu", &n);
    tot = 0;
    for (u64 i = n; i; i /= 10) a[++tot] = i % 10;
    for (int i = tot, j = 0; i > 0; --i) {
      for (int k = 9; k >= j; --k) {
        std::fill(b + 1, b + i + 1, k);
        if (calc() <= n) {
          j = k;
          break;
        }
      }
    }
    printf("Case #%d: %llu\n", tid, calc());
  }
  return 0;
}
