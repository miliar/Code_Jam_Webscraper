#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int m, n;
int A[4];

int main() {
  int T;
  scanf("%d", &T);
  for (int k = 0 ; k < T; k++) {     
     scanf("%d %d", &m, &n);
     for (int i = 0; i < n; i++) A[i] = 0;
     for (int i = 0 ;i < m; i++) {
       int t = 0;
       scanf("%d", &t);
       A[t % n] ++;
     }

     int ret  = A[0];
     if ( n == 2) {
       ret += A[1] / 2 + A[1] % 2;
     } else if (n == 3) {
       int t = min(A[1], A[2]);
       ret += t;
       int left = A[1] + A[2] - 2 * t;
       ret += left /3;
       if (left % 3 > 0) ret ++;
     } else if (n == 4) {
       ret += A[2] / 2;
       A[2] = A[2] % 2;
       int t = min(A[1], A[3]);
       ret += t;
       int left = A[1] + A[3] - 2 * t;
       if (A[2] > 0 && left >=2) {
          ret ++;
          A[2] = 0;
          left -=2;
       }
       ret += left / 4;
       left = left % 4 + A[2];
       if (left > 0) ret ++;
     }
     printf("Case #%d: %d\n", k + 1, ret);
  }
}
