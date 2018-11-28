#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int t;
  cin >> t;

  for (int ti = 0; ti < t; ti++) {
    long long d, n;
    cin >> d >> n;

    double maxTime = 0;

    for (int i = 0; i < n; i++) {
      long long k, s;
      cin >> k >> s;

      double time = double(d - k) / s;

      if (time > maxTime) {
        maxTime = time;
      }
    }

    cout << "Case #" << ti + 1 << ": " << fixed << setprecision(6) << d / maxTime << endl;
  }
}
