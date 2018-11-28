#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <cmath>

constexpr int MAX = 1004;
constexpr double pi = 3.141592653589793238462;
typedef long long ll;
typedef std::pair<ll, ll> pii;
pii A[MAX];

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i) {
      int R, H;
      scanf("%d%d", &R, &H);
      A[i].first = (ll)R * R;
      A[i].second = 2LL * (ll)R * H;
    }

    sort(A, A + N);
    std::vector<pii> v;

    ll sum = 0;
    ll best = 0;
    for (int i = 0; i < N; ++i) {
      // if (T == 10) {
      // printf("i=%d %d %d  sum=%d\n", i, A[i].first, A[i].second, sum);
      // for (int j = 0; j < (int)v.size(); ++j) {
      //   double R = sqrt(v[j].first);
      //   printf("%lf %lf\n", R, v[j].second / 2 / R);
      // }
      // }

      best = std::max(best, sum + A[i].second + A[i].first);

      auto cmp = [](pii x, pii y) { return x.second > y.second; };
      v.insert(std::lower_bound(v.begin(), v.end(), A[i], cmp), A[i]);
      sum += A[i].second;
      if ((int)v.size() > K - 1) {
        sum -= v.back().second;
        v.pop_back();
      }
    }
    printf("Case #%d: %.9lf\n", T, pi * best);
  }
  return 0;
}
