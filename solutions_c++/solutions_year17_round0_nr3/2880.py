#include <cstdio>
#include <map>

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    long N, K;
    scanf("%ld%ld", &N, &K);
    std::map<long,long> m;
    m.insert(std::pair<long,long>(N, 1));
    long ls = 0, rs = 0;
    while (K > 0) {
      auto it = m.end();
      --it;
      long x = it->first, cnt = it->second;
      m.erase(it);
      ls = (x - 1) / 2;
      rs = x - 1 - ls;
      m[ls] += cnt;
      m[rs] += cnt;
      K -= cnt;
    }
    printf("Case #%d: %ld %ld\n", t + 1, rs, ls);
  }
  return 0;
}
