#include <stdio.h>

typedef long long ll;
int main() {
  int t;
  scanf("%d",&t);
  for(int e = 0; e < t ; e++) {
    ll n,m;
    scanf("%lld %lld",&n,&m);
    ll on = n;
    ll b = 1;
    while( m > b ){
      m -= b;
      b *= 2;
    }
    ll r = on - (b-1);
    ll f = r/b, l = r/b+1;
    ll re = r%b;
    ll a;
    if (m <= re) a = l;
    else a = f;
    f = (a-1)/2;
    l = (a-1)/2 + (a-1)%2;
    printf("Case #%d: %lld %lld\n",e+1, l,f);
  }
}
