#include <stdio.h>
#include <map>
using namespace std;

#define llong long long
llong n;
int A[100], B[100];

void debug(int sz) {
  llong ret = 0;
  for (int i = sz-1; i>=0 ; i--) ret = ret * 10 + A[i];
  printf("Debug: %lld\n", ret);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0 ; t < T; t++) {     
     scanf("%lld", &n);
     int sz = 0;
     while(n > 0) {
       A[sz] = n % 10;
       B[sz] = n % 10;
       n = n / 10;
       sz ++;
     }
     for (int i = sz-1 ; i > 0 ; i--) {
        if (A[i] > A[i - 1]) A[i-1] = A[i];
     } 
     // debug(sz);
     for (int i = sz - 1; i >= 0 ; i--) {
       if (A[i] < B[i]) break;         
       if (A[i] > B[i]) {
          while(A[i+1] == A[i+2] && i + 2 < sz) i++;
	  A[i + 1] = A[i + 1] - 1;
          while (i >= 0) A[i--] = 9;
       }
     }
     llong ret = 0;
     for (int i = sz-1; i>=0 ; i--) ret = ret * 10 + A[i];
     printf("Case #%d: %lld\n", t + 1, ret);
  }
}
