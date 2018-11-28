#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
//using namespace __gnu_pbds;

#define PB push_back
#define MP make_pair
#define SZ size()
#define MEM(array, val) memset(array, val, sizeof(array))
#define Fr first
#define Sc second
#define si(a) scanf("%d", &a)
#define sl(a) scanf("%I64d", &a)
#define sd(a) scanf("%lf", &a)
#define ss(a) scanf("%s", a)

typedef long long Long;
typedef pair <int, int> Pii;
///<-------------------------------------------------END OF TEMPLATE-------------------------------------------------->

int main() {
   freopen("C-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t, ca = 1;
   si(t);

   while(t--) {
      Long N, K;
      sl(N); sl(K);

      Long a = 0, b = N, c = 0, d = 1;
      while(c+d < K) {
         K -= (c+d);
         map <Long, Long> mp;
         Long xa = a / 2, xb = b / 2;
         if(xa > 0) mp[xa] += c;
         if(a - xa - 1 > 0) mp[a - xa - 1] += c;
         if(xb > 0) mp[xb] += d;
         if(b - xb - 1 > 0) mp[b - xb - 1] += d;

         assert(mp.size() > 0 && mp.size() < 3);
         if(mp.size() == 1) {
            a = 0;
            c = 0;
            b = mp.begin()->Fr;
            d = mp.begin()->Sc;
         } else {
            a = mp.begin()->Fr;
            c = mp.begin()->Sc;
            b = mp.rbegin()->Fr;
            d = mp.rbegin()->Sc;
         }
      }
      Long ansa, ansb;
      if(K > d) {
         ansa = a / 2;
         ansb = a - ansa - 1;
      } else {
         ansa = b / 2;
         ansb = b - ansa - 1;
      }

      printf("Case #%d: %lld %lld\n", ca++, ansa, ansb);
   }

   return 0;
}
