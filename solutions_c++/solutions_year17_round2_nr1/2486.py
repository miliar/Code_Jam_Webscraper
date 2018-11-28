#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <cstdint>

using namespace std;

int64_t D, N;

int main() {
  int T = 0;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    cin >> D >> N;
    double maxT = 0;
    for (int i = 0; i < N; ++i) {
      int64_t p, s;
      cin >> p >> s;
      maxT = max(maxT, ((double)(D - p) / s));
    }
    cout << "Case #" << t << ": ";
    printf("%.6f\n", (D / maxT));
  }
}
