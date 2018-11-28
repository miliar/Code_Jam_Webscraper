#include<iostream>
#include<cstdio>
using namespace std;

int main() {
  int cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    int D, n;
    cin >> D >> n;
    double tma = 0;
    for (int i = 0; i < n; i++) {
      int k, s;
      cin >> k >> s;
      double t = (D - k) * 1.0 / s;
      if (tma < t) tma = t;
    }
    printf("Case #%d: %.6f\n", cas, D * 1.0 / tma);
  }
  return 0;
}
