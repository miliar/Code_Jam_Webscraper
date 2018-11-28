#include <algorithm>
#include <cassert>
#include <map>
#include <stdio.h>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    unsigned long long N, K;

    scanf ("%llu %llu", &N, &K);

    unsigned long long mn, mx;

    std::map<unsigned long long, unsigned long long> mp;

    mp[N] = 1;

    unsigned long long L = K;

    std::map<unsigned long long, unsigned long long>::reverse_iterator it;

    while (L != 0)
    {
      it = mp.rbegin ();

      if (it->second >= L)
      {
        assert (it->first != 0);

        break;
      }
      else
      {
        mp[it->first / 2] += it->second;
        mp[(it->first - 1) / 2] += it->second;

        L -= it->second;

        mp.erase (it->first);
      }
    }

    printf ("Case #%d: %llu %llu\n", t, it->first / 2, (it->first - 1) / 2);
  }

  return 0;
}
