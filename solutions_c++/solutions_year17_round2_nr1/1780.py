#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main() {
  int t; scanf("%d", &t);

  for (int tc = 1; tc <= t; tc++) {
    double ans = -1.0;

    int k;
    double d;
    scanf("%lf %d", &d, &k);
    for (int i = 0; i < k; i++) {
      double pos, speed;
      scanf("%lf %lf", &pos, &speed);
      double h = (d - pos) / speed;
      double predicted = d / h;
      if (ans < 0.0) ans = predicted;
      ans = min(predicted, ans);
    }
    printf("Case #%d: %.8f\n", tc, ans);
  }
}
