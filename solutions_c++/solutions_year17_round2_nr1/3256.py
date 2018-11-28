#include <climits>
#include <cstdio>
#include <iomanip>
#include <iostream>
using namespace std;

void solve(int tcase) {
  int n;
  long double d;
  long double a, b;
  cin >> d >> n;
  double min = 0;
  for (int i = 0; i < n; i++) {
    cin >> a >> b;
    double speed = (d - a) / b;
    double result = d / speed;
    if (i == 0) {
      min = result;
    } else {
      min = (result < min ? result : min);
    }
  }
  printf("Case #%d: %.6f\n", tcase, min);
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
