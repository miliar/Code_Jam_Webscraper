#include <stdio.h>
#include <map>
using namespace std;

#define llong long long
llong n, k;

map<llong, llong> cache;

llong large(llong a, llong sum) {
   if (cache.find(a) != cache.end()) {
      return cache.find(a)->second;
   }
   
   if (a <= sum) return 0;
   llong ret = 1 + large(a/2, sum) + large((a-1) /2, sum); 
   cache[a] = ret;
   return ret;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0 ; t < T; t++) {     
     scanf("%lld%lld", &n, &k);
     llong left = 0, right = n, ret = 0;
     while(left <= right) {
        llong mid = (left + right) / 2;
        cache.clear();
        // printf("%lld %lld %lld\n", n, mid, large(n, mid));
        if (large(n, mid) >= k) {
           ret = mid;
           left = mid + 1;
        } else {
           right = mid - 1;
        }
     }
     printf("Case #%d: %lld %lld\n", t + 1, (ret + 1)/2, ret/ 2);
  }
}
