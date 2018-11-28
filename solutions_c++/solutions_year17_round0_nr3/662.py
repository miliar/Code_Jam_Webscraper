#include <stdio.h>
#include <map>
using namespace std;

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    long long N, K;
    scanf("%lld %lld\n", &N, &K);
    map<long long, long long> m;
    m[N] = 1;
    long long ls, rs;
    while (K > 0) {
      auto it = --m.end();
      long long n = it->second;
      long long s = it->first;
      m.erase(it, m.end());
      long long mid = s / 2ll;
      ls = mid;
      rs = s - ls - 1ll;
      m[ls] += n;
      m[rs] += n;
      K -= n;
    }
    printf("Case #%d: %lld %lld\n", t, ls, rs);
  }
}