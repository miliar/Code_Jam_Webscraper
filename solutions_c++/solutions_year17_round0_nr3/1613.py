#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll t, T, n, k, mn, mx, v;
map<ll, ll> q;

int main() {
  scanf("%lld", &T);
  while(t++ < T) {
    scanf("%lld%lld", &n, &k);
    q.clear();
    q[n] = 1;

    while(k > 0) {
      ll v = q.rbegin()->first;
      ll c = q.rbegin()->second;
      q.erase(v);

      mx = v/2;
      mn = (v-1)/2;

      q[mx] += c;
      q[mn] += c;

      k -= c;
    }

    printf("Case #%lld: %lld %lld\n", t, mx, mn);
  }
  return 0;
}
