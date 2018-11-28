#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    long long d, n; cin >> d >> n;
    double r = 0;
    for (int i = 0; i < n; i++) {
      long long k, s; cin >> k >> s;
      r = max(r, (1.0 * d - k) / s);
    }
    cout << "Case #" << c << ": " << fixed << setprecision(8) << d / r << endl;
  }
  return 0;
}
