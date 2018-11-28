#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<ll,ll>;

ll N, K;

pii solve() {
  if (K == 1) {
    return {N/2, (N-1)/2};
  }
  int level = log2(K);
  ll small = 0, big = 1;
  for (int i = 0; i < level; ++i, N/=2) {
    if (N % 2 == 1) {
      big = 2*big + small;
    } else {
      small = 2*small + big;
    }
  }
  K -= (1 << (level));
  if (K >= big) {
    return {(N-1)/2, (N-2)/2};
  } else {
    return {N/2, (N-1)/2};
  }
}



int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> N >> K;
    ll a, b; tie(a,b) = solve();
    printf("Case #%d: %lld %lld\n", i, a, b);
  }
  return 0;
}
