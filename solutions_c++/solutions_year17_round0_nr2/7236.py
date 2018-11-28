#include <bits/stdc++.h>
using namespace std;

typedef long long Long;

Long N;
Long dig[20], ii = 0;
Long res[20];

bool oka(int i, Long d) {
   if(res[i+1] > d) return false;
   Long a = 0;
   for(int j = ii; j >= 1; j--) {
      a = 10*a + dig[j];
   }
   Long b = 0;
   for(int j = ii; j > i; j--) {
      b = 10*b + res[j];
   }
   for(int j = i; j >= 1; j--) {
      b = 10*b + d;
   }
   return b <= a;
}

void work() {
   ii = 0;
   while(N > 0) {
      dig[++ii] = N % 10;
      N /= 10;
   }
   // cerr << "ii = " << ii << "\n";
   dig[ii+1] = res[ii+1] = 0;
   for(int i = ii; i >= 1; i--) {
      for(int d = 9; d >= 0; d--) {
         if(oka(i,d)) {
            res[i] = d;
            break;
         }
      }
   }
}

int main() {
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      scanf("%lld", &N);
      work();
      Long rs = 0;
      for(int i = ii; i >= 1; i--) {
         rs = 10*rs + res[i];
      }
      printf("Case #%d: %lld\n", cs, rs);
   }
}
