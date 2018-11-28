#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int N;
    double D;
    scanf("%lf %d", &D, &N);
    double Time = 0.0;
    for (int h = 0; h < N; h++) {
        double S, V;
        scanf("%lf %lf", &S, &V);
        Time = std::max(Time, (D-S) / V);
    }
    printf("Case #%d: %lf\n", t, D/Time);
  }
  return 0;
}
