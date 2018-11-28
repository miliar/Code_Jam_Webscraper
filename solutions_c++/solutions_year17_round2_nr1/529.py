#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;
using namespace std::chrono;

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout << fixed << setprecision(10);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int d, n;
    cin >> d >> n;
    long double max_time = 0;
    for (int i = 0; i < n; ++i) {
      int p, s;
      cin >> p >> s;
      long double cur = 1.0 * (d - p) / s;
      max_time = max(max_time, cur);
    }

    cout << "Case #" << test << ": " << d / max_time << endl;
  }


  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
