#include <iostream>

#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <vector>

#include <algorithm>
#include <limits>

#include <cmath>

using namespace std;

int main() {

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";

    int D, N;
    cin >> D >> N;

    double min = numeric_limits<double>::max();
    for (int n = 0; n < N; n++) {
      int k;
      int s;
      cin >> k >> s;
      double v = 1.0 * D * s / (D - k);
      if (v < min)
	min = v;
    }

    cout.precision(numeric_limits<double>::max_digits10);
    cout << fixed << min << endl;
  }
  
  return 0;
}
