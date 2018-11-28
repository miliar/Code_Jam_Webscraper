#include <cstdio>
#include <cstring>
#include <cstdio>
#include <string>
#include <queue>
#include <vector>
using namespace std;

inline long long big(long long x) { return x>>1; }
inline long long small(long long x) { return x&1 ? x>>1 : (x>>1)-1; }

int main() {
    int T;
    scanf("%d", &T);
    for(int tc = 1;tc <= T;++tc) {
      printf("Case #%d: ", tc);

      long long n, k; scanf("%lld%lld", &n, &k);

      if(k==1) {
        printf("%lld %lld\n", big(n), small(n));
        continue;
      }
      long long p = 2, m = k-1;
      long long a = big(n), b = small(n);
      long long sa = 1, sb = 1;

      while(m) // 1-based
      {
          if(m <= p)
          {
            // if(n - p >= p) { // bukan baris terakhir
            // } else {}
            if(m <= sa) printf("%lld %lld\n", big(a), small(a));
            else printf("%lld %lld\n", big(b), small(b));
            break;
          } else {
            m -= p;
            p <<= 1;

            long long na = big(a);
            long long nb = small(b);
            long long nsa = 0, nsb = 0;

            // bigA
            nsa += sa;

            // smallA
            if(small(a) == na) nsa += sa;
            else nsb += sa;

            // smallB
            nsb += sb;

            // bigB
            if(big(b) == nb) nsb += sb;
            else nsa += sb;

            a = na; b = nb; sa = nsa; sb = nsb;
            // printf("%lld %lld(%lld) %lld(%lld)\n", p, )
          }
    }

  }
}
