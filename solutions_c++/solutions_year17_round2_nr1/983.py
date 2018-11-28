#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int D, N;
    cin >> D >> N;

    double max_t = 0;
    for (int i = 0; i < N; i++) {
      int k, v;
      cin >> k >> v;

      double t = 1.0 * (D - k) / v;
      if (t > max_t) {
        max_t = t;
      }
    }

    cout << setprecision(9);
    cout << "Case #" << (t + 1) << ": " << (D / max_t) << endl;
  }

  return 0;
}
