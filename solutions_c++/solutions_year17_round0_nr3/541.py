#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <set>
#include <map>
#include <array>
#include <climits>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

typedef unsigned long long u64;


int main() {
  int t;
  cin >> t;

  for (int i_test = 0; i_test < t; ++i_test) {

    u64 n, k;
    cin >> n >> k;

    u64 level = 1;
    u64 passed = 0;
    u64 min, max;
    while (passed < k) {
      u64 count1 = (n - passed) % level;
      if (k - passed <= count1) {
        u64 len = (n - passed) / level + 1;
        min = (len - 1) / 2;
        max = len - 1 - min;
        break;
      } else if (k - passed <= level) {
        u64 len = (n - passed) / level;
        min = (len - 1) / 2;
        max = len - 1 - min;
        break;
      } else {
        passed += level;
      }

      level *= 2;
    }

    cout << "Case #" << i_test + 1 << ": " << max << " " << min << endl;
  }

  return 0;
}
