#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <queue>

int main()
{
  int T;
  std::cin >> T;
  for (int i = 0; i < T; i++) {
    uint64_t N, K;
    std::cin >> N >> K;
    std::priority_queue <uint64_t> q;
    q.push (N);
    uint64_t l,r;
    for (uint64_t j = 0; j < K ; j++) {
      uint64_t tmp = q.top () - 1;
      q.pop ();
      l = tmp / 2;
      r = tmp - (tmp / 2);
      q.push(l);
      q.push(r);
    }
    std::cout << "Case #" << i + 1 << ": ";
    std::cout << std::max(l,r) << " " << std::min(l,r) << std::endl;
  }
  return 0;
}
