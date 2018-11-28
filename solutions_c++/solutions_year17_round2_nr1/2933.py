#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <limits>
#include <list>
#include <unordered_set>
#include <iomanip>

using namespace std;

#ifdef DEBUG
  #define log(...) \
    cout << __VA_ARGS__;
#else
  #define log(...)
#endif

struct Horse {
  uint64_t k;
  double s;
};

double calculateSpeed(uint64_t destination, const std::vector<Horse>& horses)
{
  double maximum = -1;

  for (auto& horse : horses) {
    double t = (destination - horse.k) / horse.s;
    double max = destination / t;

    if (maximum < 0 || maximum > max) {
      maximum = max;
    }
  }

  return maximum;
}

int main() {
    int t;
    uint64_t D, N;

    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> D >> N;
        std::vector<Horse> horses;
        for (int i = 0; i < N; ++i) {
            Horse h;
            cin >> h.k >> h.s;
            horses.push_back(h);
        }

        cout << "Case #" << i << ": " << std::fixed << std::setprecision (6) << calculateSpeed(D, horses) << endl;
        // calculate(k, n, &x, &y);
        // cout << "Case #" << i << ": " << x << " " << y << endl;
    }
    return 0;
}
