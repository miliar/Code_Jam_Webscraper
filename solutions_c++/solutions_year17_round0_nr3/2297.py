#include <bits/stdc++.h>
using namespace std;

typedef pair<long long, long long> pll;

int main(void) {

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d: ", cas);

    long long n, K; scanf("%lld %lld", &n, &K);

    set<pll> SET[2];
    int next = 0, now = 1;
    SET[now].clear();
    SET[now].insert(pll(n, 1));
    while (true) {
      // printf("size = %d\n", SET[now].size());
      long long total = 0;
      for (const auto &it : SET[now]) {
        total += it.second;
      }
      if (K <= total) {
        for (auto it = SET[now].rbegin(); it != SET[now].rend(); ++it) {
          if (K <= it->second) {
            long long tmp = it->first-1;
            printf("%lld %lld\n", tmp - tmp / 2, tmp / 2);
            break;
          }
          K -= it->second;
        }
        break;
      } else {
        SET[next].clear();
        map<long long, long long> count;
        for (const auto &it : SET[now]) {
          count[it.first / 2] += it.second;
          count[(it.first - 1) / 2] += it.second;
        }
        for (const auto &it : count) {
          SET[next].insert(it);
        }
        K -= total;
      }
      swap(now, next);
    }

  }

  return 0;
}