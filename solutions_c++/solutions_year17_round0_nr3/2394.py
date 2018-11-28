#include <bits/stdc++.h>
using namespace std;

int main ()
{
  int t, i;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    int64_t n, k;
    scanf ("%lld%lld", &n, &k);
    map<int64_t, int64_t> m;
    m[n] = 1;
    while (k > 0) {
      map<int64_t, int64_t>::reverse_iterator itr = m.rbegin ();
      if (itr->second >= k) printf ("Case #%d: %lld %lld\n", i,
        (itr->first + 0) / 2, (itr->first - 1) / 2);
      k -= itr->second;
      m[(itr->first - 1) / 2] += itr->second;
      m[ itr->first      / 2] += itr->second;
      m.erase (--itr.base());
    }
  }
  return 0;
}
