#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cstdint>
#include <cmath>

using namespace std;

uint64_t solve(string m) {
  int len = m.size();
  int target = -2;
  for (int i = len - 2; i >= 0; --i) {
    if (m[i] > m[i + 1]) {
      target = i;
    } else if (m[i] == m[i + 1] && target == i + 1) {
      target = i;
    }
  }
  if (target != -2) {
    --m[target];
    for (int i = target + 1; i < len; ++i) {
      m[i] = '9';
    }
  }
  return stoull(m);
}

int main() {
  int n = 0;
  scanf("%d\n", &n);
  uint64_t m = 0;
  string line;
  for (int i = 0; i < n; ++i) {
    getline(cin, line);
    uint64_t ans = solve(line);
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
}
