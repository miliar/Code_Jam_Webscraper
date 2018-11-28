#include <bits/stdc++.h>
using namespace std;

int main() {
  int t; scanf("%d", &t);
  for(int _i=1; _i<=t; _i++) {
    int d, n; scanf("%d %d", &d, &n);
    double min_time=0;
    for(int i=0; i<n; i++) {
      int k, s; scanf("%d %d", &k, &s);
      min_time = max(min_time, ((double)d-(double)k)/(double)s);
    }
    printf("Case #%d: %lf\n", _i, (double)d/min_time);
  }
}
