#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
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
typedef pair<string, string> pss;

const int sz = 1e5;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string pancake;
    int k;

    cin >> pancake >> k;

    bool possible = true;
    int steps = 0;

    for (int i = 0, e = pancake.size(); i < e; ++i) {
      if (pancake[i] == '+') {
        continue;
      }

      if (i + k > e) {
        possible = false;
        break;
      }

      ++steps;

      for (int j = i; j < i + k; ++j) {
        pancake[j] = pancake[j] == '+' ? '-' : '+';
      }
    }

    if (possible) {
      cout << steps << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}

