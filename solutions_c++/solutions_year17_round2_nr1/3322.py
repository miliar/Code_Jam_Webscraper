#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll INF = 1e18;
ll t, T, d, n, k, s;
long double ans;

int main() {
  scanf("%lld", &T);
  while(t++ < T) {
    scanf("%lld%lld", &d, &n);
    ans = INF;
    for(int i=0; i<n; ++i) {
      scanf("%lld%lld", &k, &s);
      ans = min(1.0L*d*s/(d-k), ans);
    }
    printf("Case #%lld: %Lf\n", t, ans);
  }
  return 0;
}
