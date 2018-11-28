#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

double hl[1010][2];

int main() {
  int t;

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    double d;
    int n;
    scanf("%lf %d", &d, &n);
    double mti = 0.0;
    for (int i = 0; i < n; i++) {
      scanf("%lf %lf", &hl[i][0], &hl[i][1]);
      double ti = ((d - hl[i][0]) / hl[i][1]);
      mti = max(mti, ti);
    }
    printf("Case #%d: %.6f\n", o + 1, (d / mti));
  }

  return 0;
}
