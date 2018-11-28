#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

vector<uint64_t> solve(uint64_t r, uint64_t p) {
  if (p == 1) {
    if (r % 2 == 0) {
      return { r / 2, r / 2 - 1 };
    } else {
      return { r / 2, r / 2 };
    }
  }
  if (r % 2 == 0) {
    if (p % 2 == 0) {
      return solve(r / 2, p / 2);
    } else {
      return solve(r / 2 - 1, p / 2);
    }
  } else {
    return solve(r / 2, p / 2);
  }
}

int main() {
  int n = 0;
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    uint64_t p, r;
    scanf("%llu %llu\n", &r, &p);
    vector<uint64_t> ans = solve(r, p);
    cout << "Case #" << i + 1 << ": " << ans[0] << " " << ans[1] << endl;
  }
}
