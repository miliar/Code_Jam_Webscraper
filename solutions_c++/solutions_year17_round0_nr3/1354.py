#include <cstdio>
#include <map>

using namespace std;
typedef long long int ll;

int t;
ll n, k;
map<ll, ll> c;

int main()
{
  scanf("%d", &t);
  for(int i = 0; i < t; ++i) {
    scanf("%lld %lld", &n, &k);
    c.clear();
    c[n] = 1;
    while(true) {
      auto it = c.end();
      --it;
      ll len = it->first;
      ll count = it->second;
      k -= count;
      if(k <= 0) {
        if(len%2) {
          printf("Case #%d: %lld %lld\n", i+1, (len-1)/2, (len-1)/2);
        }
        else {
          printf("Case #%d: %lld %lld\n", i+1, len/2, len/2-1);
        }
        break;
      }

      if(len%2) {
        c[(len-1)/2] += 2*count;
      }
      else {
        c[len/2-1] += count;
        c[len/2] += count;
      }
      c.erase(it);
    }
  }
  return 0;
}
