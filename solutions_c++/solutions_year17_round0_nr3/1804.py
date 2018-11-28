#include <cstdio>
#include <map>
using namespace std;
typedef long long ll;
int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    ll n, k;
    scanf("%lld%lld", &n, &k);
    map<ll, ll> m;
    m[n] = 1;
    while (true) {
      auto it = prev(m.end());
      if (it->second < k) {
        auto p = *it;
        m.erase(it);

        k -= p.second;
        m[(p.first - 1) / 2] += p.second;
        m[p.first / 2] += p.second;
      } else {
        printf("Case #%d: %lld %lld\n", ti + 1, it->first / 2, (it->first - 1) / 2);
        break;
      }
    }
  }
  return 0;
}
