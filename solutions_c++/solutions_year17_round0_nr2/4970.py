#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
  vector<int> N_vec_r;
  vector<int> min_r;
  int64_t T, N, m, min, d;

  cin >> T;
  for (int64_t i = 1; i <= T; ++i) {
    N_vec_r.clear();
    min_r.clear();
    cin >> N;
    m = N;

    while (m > 0) {
      N_vec_r.push_back(m % 10);
      m /= 10;
    }
 
    min_r.push_back(N_vec_r[0]);
    for (int64_t j = 1; j < N_vec_r.size(); ++j) {
      min = min_r[j - 1];
      d = N_vec_r[j];
      if (d > min) {
        for (int64_t k = 0; k < j; ++k) {
          min_r[k] = 9;
        }
        min_r.push_back(d - 1);
      } else {
        min_r.push_back(d);
      }
    }

    cout << "Case #" << i << ": ";
    bool started = false;
    for (int64_t j = min_r.size() - 1; j > 0; --j) {
      if (min_r[j] > 0) {
        started = true;
      }
      if (started) {
        cout << min_r[j];
      }
    }
    cout << min_r[0] << endl;
  }

  return 0;
}
