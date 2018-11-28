#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int t, n, d;

int main(void) {
  while(scanf("%d", &t) != -1) {
    for(int tt = 0; tt < t; tt += 1) {
      scanf("%d%d", &d, &n);
      int k, s;
      long double minSpeed = 1e15;
      for(int i = 0; i < n; i += 1) {
        scanf("%d%d", &k, &s);
        minSpeed = MIN(minSpeed, s * 1.0 * d * 1.0 / (d - k));
      }
      printf("Case #%d: %.9Lf\n", tt + 1, minSpeed);
    }
  }
  return 0;
}
