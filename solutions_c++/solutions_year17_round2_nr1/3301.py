#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <numeric>
#include <functional>
using namespace std;

typedef unsigned long long int llui;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<string, string> pss;

const int sz = 1e5;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";

    int D, N;
    cin >> D >> N;

    vector<pdd> pos(N);

    for (int i = 0; i < N; ++i) {
      cin >> pos[i].first >> pos[i].second;
    }

    double l = 0;
    double r = numeric_limits<double>::max();

    while (r - l > 1e-6) {
      double m = (l + r) / 2;
      if (m == l) {
        break;
      }

      bool possible = true;
      for (int i = 0; i < N; ++i) {
        double t = (D - pos[i].first) / pos[i].second;
        if (m > (pos[i].first / t) + pos[i].second) {
          possible = false;
          break;
        }
      }

      if (possible) {
        l = m + 1e-6;
      } else {
        r = m;
      }
    }

    cout << fixed << setprecision(8) << l << endl;
  }
}

