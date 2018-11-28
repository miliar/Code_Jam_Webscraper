#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T;
long long D, N;
vector<pair<int, int> > hs;
int main() {
  scanf("%d\n", &T);
  for (int TT = 1; TT <= T; TT++) {
    scanf("%lld%lld", &D, &N);
    hs.resize(N);
    double ans  = 1e100;
    for (int i = 0; i < N; i++) {
      scanf("%d%d", &hs[i].first, &hs[i].second);
      ans = min(ans, D / ((D - hs[i].first) / double(hs[i].second)));
    }
    printf("Case #%d: %.8lf\n", TT, ans);

  }
  return 0;
}
