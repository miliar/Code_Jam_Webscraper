#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <map>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    llint N, K;
    scanf("%lld %lld", &N, &K);

    map<llint, llint> gaps_cnt;
    gaps_cnt[N] = 1;
    
    llint last_gap = -1;
    while (K > 0) {
      auto largest_gap = *gaps_cnt.rbegin();
      last_gap = largest_gap.first;
      K -= largest_gap.second;

      gaps_cnt.erase(largest_gap.first);

      if (largest_gap.first / 2 > 0) {
        gaps_cnt[largest_gap.first / 2] += largest_gap.second;
      }
      if ((largest_gap.first - 1) / 2 > 0) {
        gaps_cnt[(largest_gap.first - 1) / 2] += largest_gap.second;
      }
    }
    
    printf("Case #%d: ", tp);
    printf("%lld %lld\n", last_gap / 2, (last_gap - 1) / 2);
  }
  return 0;
}
