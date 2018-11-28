#include <stdio.h>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

int T;

pll sizes(ll s) {
  if (s%2 == 0)
    return pll(s/2 - 1, s/2);
  return pll(s/2, s/2);
}

pair<ll, ll> f(ll s1, ll s2, ll m1, ll m2, ll K) {
  if (m2 == 0) {
    if (s1%2 == 0) {
      s2 = s1 / 2 - 1;
      s1 = s1 / 2;

      if (m1 >= K)
        return pll(s2, s1);
      return f(s1, s2, m1, m1, K - m1);
    } else {
      s1 = s1 / 2;
      
      if (m1 >= K)
        return pll(s1, s1);
      return f(s1, s2, 2 * m1, 0, K - m1);
    }
  }

  if (m1 >= K) {
    return sizes(s1);
  }
  
  if (m1 + m2 >= K) {
    return sizes(s2);
  }

  if (m1 + m2 < K) {
    if (s1%2 == 0) {
      return f(s1/2, s1/2 - 1, m1, m1 + 2 * m2, K - m1 - m2);
    } else {
      return f(s1/2, s1/2 - 1, 2 * m1 + m2, m2, K - m1 - m2);
    }
  }
}

int main() {
  scanf("%d", &T);

  for (int t = 1;t <= T;++t) {
    ll N, K;
    scanf("%lld %lld", &N, &K);

    pll ans = f(N, 0, 1, 0, K);

    printf("Case #%d: %lld %lld\n", t, ans.second, ans.first);
  }
  return 0;
}
