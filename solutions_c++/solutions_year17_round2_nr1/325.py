#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

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
    int D, N;
    scanf("%d %d", &D, &N);

    vector<pair<int, int>> horses;
    REP(i, N) {
      int K, S;
      scanf("%d %d", &K, &S);
      horses.push_back({K, S});
    }

    sort(horses.begin(), horses.end());
    double ans = 0;
    for (int i = N-1; i >= 0; --i) {
      ans = max(ans, (D - horses[i].first) * 1.0 / horses[i].second);
    }
    ans = D / ans;
    printf("Case #%d: ", tp);
    printf("%.10lf\n", ans);
  }
  return 0;
}
