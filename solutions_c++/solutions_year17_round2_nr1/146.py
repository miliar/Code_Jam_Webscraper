// A.cpp

#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    int n, d, k, s;
    cin >> d >> n;
    double tmax = 0;
    for (int i = 0; i < n; i++) {
      cin >> k >> s;
      double t = 1.0 * (d - k) / s;
      if (t > tmax) {
        tmax = t;
      }
    }
    printf("Case #%d: %.8lf\n", ++kase, d / tmax);
  }
  return 0;
}
