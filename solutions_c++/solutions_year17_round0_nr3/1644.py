#include <cstdio>
#include <map>

typedef long long i64;

const int N = 1000000 + 10;

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    std::map<i64, i64> q;
    i64 n, k;
    scanf("%lld%lld", &n, &k);
    q[n + 1] = 1;
    while (1) {
      i64 x = q.rbegin()->first, y = q.rbegin()->second;
      q.erase(x);
      k -= y;
      i64 a = x / 2, b = x - a;
      if (k <= 0) {
        printf("Case #%d: %lld %lld\n", tid, b - 1, a - 1);
        break;
      }
      q[a] += y;
      q[b] += y;
    }
  }
  return 0;
}
