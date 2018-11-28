#include <algorithm>
#include <cinttypes>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;

int T, N, K;
double U;
vector<double> p;

int main(int argc, char *argv[]) {

  cout << fixed;
  cout << setprecision(20);

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    p.clear();
    cin >> N;
    cin >> K;
    p.resize(N);
    cin >> U;
    for (int j = 0; j < N; ++j) {
      cin >> p[j];
    }
    sort(p.begin(), p.end());
    int k = 0;
    while (U > 0.0 && k < N - 1) {
      if (U > (k + 1) * (p[k + 1] - p[k])) {
        U -= (k + 1) * (p[k + 1] - p[k]);
        for (int l = 0; l <= k; ++l) {
          p[l] = p[k + 1];
        }
      } else {
        double v = U / (k + 1);
        for (int l = 0; l <= k; ++l) {
          p[l] += v;
        }
        U = 0.0;
      }
      ++k;
    }
    if (U > 0.0) {
      for (int l = 0; l < N; ++l) {
        p[l] += U / N;
      }
    }

    double prod = 1.0;
    for (int j = 0; j < N; ++j) {
      prod *= p[j];
    }

    if (prod > 1.0) {
      prod = 1.0;
    }

    cout << "Case #" << i << ": " << prod << endl;
  }

  return 0;
}
