#include <cstdio>
#include <set>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
typedef long long ll;

int _;
ll n, k, a, b;


int main() {
  scanf("%d", &_);
  REP(t, _) {
    scanf("%lld%lld", &n, &k);

    ll last = -1;
    ll a = -1, b = n;
    ll acnt = 0, bcnt = 1;
    while (k > 0) {
//      printf("| k=%lld   a=%lld (%lld)  b=%lld (%lld)\n",
//          k, a, acnt, b, bcnt);
      bool bit = b%2 == 0;
      if (a == -1) {
        last = b;
        k -= bcnt;

        b = (b-1)/2;
        if (bit) {
          a = b; b++;
          acnt = bcnt;
        } else {
          bcnt *= 2;
        }

      } else {
        last = b;
        k -= bcnt;
        if (k > 0) {
          last = a;
          k -= acnt;
        }

        b = b/2; a = (a-1)/2;
        if (bit) acnt += acnt+bcnt;
        else bcnt += acnt+bcnt;

      }
    }

    printf("Case #%d: %lld %lld\n", t+1, last/2, (last-1)/2);
  }
}
