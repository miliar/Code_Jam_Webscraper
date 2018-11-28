#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;
typedef map<ll, ll>::iterator iter;
map<ll, ll> s;

int main(void) {
  int t;
  scanf("%d", &t);
  for (int id = 1; id <= t; ++id) {
    ll n, k;
    scanf("%I64d%I64d", &n, &k);
    s.clear();
    s[n] = 1;
    while (k > 1) {
      iter it = --s.end();
      ll num = min(k - 1, it->second);
      ll llen = (it->first - 1) / 2;
      ll rlen = it->first - 1 - llen;
      if (llen) {
        s[llen] += num;
      }
      if (rlen) {
        s[rlen] += num;
      }
      it->second -= num;
      if (it->second == 0) {
        s.erase(it);
      }
      k -= num;
    }
    iter it = --s.end();
    ll llen = (it->first - 1) / 2;
    ll rlen = it->first - 1 - llen;
    printf("Case #%d: %I64d %I64d\n", id, rlen, llen);
  }
  return 0;
}
