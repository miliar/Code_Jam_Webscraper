#include <cstdio>
#include <cassert>
#include <map>
using namespace std;
typedef long long int ll;

void runSLOW() {
  ll N,K;
  scanf("%lld%lld", &N, &K);
  map<ll,ll,greater<ll> > m;
  m[N]=1ll;
  for (;;) {
    ll spl=m.begin()->first;
    if (m.begin()->second==1ll) m.erase(m.begin()); else --m.begin()->second;
    ll vmax=spl/2ll,vmin=(spl-1ll)/2ll;
    if (vmax) ++m[vmax];
    if (vmin) ++m[vmin];
    if (--K==0ll) {
      printf("%lld %lld\n", vmax, vmin);
      return;
    }
  }
}
void run() {
  ll N,K;
  scanf("%lld%lld", &N, &K);
  ll oN=1ll,oN1=0ll;
  for (;;) {
    if (K<=oN1) { printf("%lld %lld\n", (N+1ll)/2ll, N/2ll); return; }
    if (K<=oN1+oN) { printf("%lld %lld\n", N/2ll, (N-1ll)/2ll); return; }
    K-=oN1+oN;
    if (N%2ll) oN=2ll*oN+oN1;
    else oN1=2ll*oN1+oN;
    N=(N-1ll)/2ll;
  }
}
int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
/* 
 */
