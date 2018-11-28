#include <cstdio>

int main() {
  int t;
  scanf("%d", &t);
  
  for (int tcase = 1; tcase <= t; tcase++) {
    double d;
    int n;
    
    scanf("%lf %d", &d, &n);
    
    
    double res = 0;
    for (int i = 0; i < n; i++) {
      double k, s;
      scanf("%lf %lf", &k, &s);
      
      if ( (d - k) / s > res) {
        res = (d - k) / s;
      }
    }
    
    printf("Case #%d: %.6lf\n", tcase, d / res);
  }
  return 0;
}
