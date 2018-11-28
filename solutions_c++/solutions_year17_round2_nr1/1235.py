#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {
    long long d, num_horses; cin >> d >> num_horses;
    double max_time = 0;
    for(int i = 0; i<num_horses; ++i) {
      long long k, s;
      cin >> k >> s;
      double time_to_end = (d - k) * 1.0 / s;
      max_time = max(max_time, time_to_end);
    }
    cout << fixed;
    cout << "Case #" << test+1 << ": " << (d * 1.0) / max_time << endl;
  }
}
