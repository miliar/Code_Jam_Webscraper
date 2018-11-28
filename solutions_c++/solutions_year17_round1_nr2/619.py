#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define llong long long

int m, n;
llong A[128], B[64][64], C[64];

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0 ; t < T; t++) {     
     scanf("%d %d", &m, &n);
     for (int i = 0 ;i < m; i++) {
       scanf("%lld", &A[i]);
     }
     for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) { 
          scanf("%lld", &B[i][j]);
        }
       sort(B[i], B[i] + n);
       reverse(B[i], B[i] + n);
       C[i] = 0;
     }
     llong large = (B[0][0] * 10) / (A[0] * 9);
     for (int i = 0; i < m; i ++) {
        large = min(large, B[i][0] * 10 /(9 * A[i]));
     }

     int ret = 0;
     while (large > 0) {
       // printf("-- %d\n", large);
       bool brk  = false;
       bool finish = false;
       for (int i = 0; i < m; i++) {
          if (B[i][C[i]] * 10 > large * A[i] * 11) {
             // printf("too large\n");
             C[i] ++;
             brk = true;
             if (C[i] >= n) { 
               finish  = true;
             }
             break;
         }
       }
       if (finish) break;
       if (brk) continue;

       for (int i = 0; i < m; i++) {
          if (B[i][C[i]] * 10 < large * A[i] * 9) {
             // printf("too smale\n");
             large = 10 * B[i][C[i]] / (9 * A[i]);
             brk = true;
             break;
          }
       }
       if (finish) break;
       if (brk) continue;
       
       ret ++;
       for (int i = 0; i < m; i++) {
          C[i] ++;
          if (C[i] >= n) {
           finish = true;
           break;
          }
       }
       if (finish) break;
       if (brk) continue;
     }
     printf("Case #%d: %d\n", t + 1, ret);
  }
}
