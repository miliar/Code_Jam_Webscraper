#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>

#define _USE_MATH_DEFINES

using namespace std;
typedef long long ll;
const int MAXN = 1000 + 100;
int T, N, K;
pair<ll, ll> pancakes[MAXN];
ll dp[MAXN][MAXN];
ll best[MAXN];
ll area(ll r) {
  return r * r;
}

ll side(ll r, ll h) {
  return h * 2 * r;
}

int main() {
  scanf("%d", &T);

  for (int t = 1;t <= T;++t) {
    scanf("%d %d", &N, &K);
    
    for (int i = 0;i < N;++i)
      scanf("%lld %lld", &pancakes[i].first, &pancakes[i].second);
    
    for (int i = 0;i < MAXN;++i) {
      for (int j =  0;j < MAXN;++j) {
        dp[i][j] = 0;
      }
      best[i] = 0;
    }

    sort(pancakes, pancakes + N);
    
    for (int i = 0;i < N;++i) {
      ll r = pancakes[i].first;
      ll h = pancakes[i].second;
      for (int j = 1;j <= K;++j) {
        dp[i][j] = side(r, h) + best[j - 1]; 
      }

      for (int j = 1;j <= K;++j) {
        best[j] = max(best[j], dp[i][j]);
      }
    }

    ll ans = 0; 
    for (int i = 0;i < N;++i) {
      ans = max(ans, dp[i][K] + area(pancakes[i].first));
    }
    

    printf("Case #%d: %.10Lf\n", t, M_PI * (long double)ans);
    
  }
  return 0;
}
