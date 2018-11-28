#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
using namespace std;

void solve() {
  long long N, K;
  scanf("%lld %lld", &N, &K);

  // gap size => #
  map<long long,long long> gaps;
  gaps[N] = 1;

  while (true) {
    auto it = --gaps.end();
    long long gap = it->first, cnt = it->second;
    gaps.erase(it);

    long long small_gap = (gap-1)/2;
    long long big_gap = gap - 1 - small_gap;

    if (cnt >= K) {
      printf("%lld %lld\n", big_gap, small_gap);
      return;
    }

    K -= cnt;

    if (gaps.find(small_gap) != gaps.end())
      gaps[small_gap] += cnt;
    else
      gaps[small_gap] = cnt;

    if (gaps.find(big_gap) != gaps.end())
      gaps[big_gap] += cnt;
    else
      gaps[big_gap] = cnt;
  }
}

int main() {
    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
      printf("Case #%d: ", t+1);
      solve();
    }
}