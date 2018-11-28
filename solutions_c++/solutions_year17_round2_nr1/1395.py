#include <assert.h>
#include <iostream>
#include <cmath>

using namespace std;


const double EPS = 1e-6;
const int N = 1024;
int k[N], s[N];
int d, n;

int main() {
  int T; cin >> T;
  for (int test = 0; test < T; ++test) {
    cin >> d >> n;
    double t = 0;
    for (int i = 0; i < n; ++i) {
      cin >> k[i] >> s[i];
      t = max(t, 1.0 * (d - k[i]) / s[i]);
    }
    printf("Case #%d: %.6lf\n", test + 1, d / t);
  }
}
