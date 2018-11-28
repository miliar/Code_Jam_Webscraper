/* Copyright 2017 Yusuf Hussein
 */
#include <iostream>
#include <map>

int64_t solve(int64_t n, int64_t k) {
  std::map<int64_t, int64_t> mp;
  mp[n] = 1;
  while (true) {
    int64_t num = mp.rbegin()->first;
    int64_t cnt = mp.rbegin()->second;
    if (k <= cnt) {
      return num;
    }
    k -= cnt;
    mp[(num - 1) >> 1] += cnt;
    mp[num >> 1] += cnt;
    mp.erase(num);
  }
  return 0;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int64_t n, k;
    std::cin >> n >> k;
    int64_t ans = solve(n , k);
    std::cout << "Case #" << t << ": "
      << ans / 2 << ' ' << (ans - 1) / 2 << '\n';
  }
}
