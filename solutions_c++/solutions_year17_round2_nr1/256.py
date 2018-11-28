#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  cout << fixed;
  cout.precision(20);

  for (int tst = 0; tst < T; tst++) {
    int d, n;
    cin >> d >> n;
    double res = 1e18;

    for (int i = 0; i < n; i++) {
      int k, s;
      cin >> k >> s;
      res = min(res, double(d) * s / (d - k));
    }
    cout << "Case #" << tst + 1 << ": " << res << '\n';
  }
}
