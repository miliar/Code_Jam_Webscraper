#include <iostream>
#include <queue>

int main(int argc, char *argv[]) {
  uint64_t T, N, K;
  std::cin >> T;

  for (unsigned int t = 0; t < T; ++t) {
    std::priority_queue<uint64_t> stalls;
    std::cin >> N >> K;
    stalls.push(N);

    for (uint64_t i = 0; i < (K - 1); ++i) {
      const auto curStall = stalls.top();
      stalls.pop();
      if ((curStall - 1) % 2 == 0) {
        const auto addStall = (curStall - 1) / 2;
        stalls.push(addStall);
        stalls.push(addStall);
      } else {
        const auto addStall = curStall / 2;
        stalls.push(addStall);
        stalls.push(addStall - 1);
      }
    }
    std::cout << "Case #" << t + 1 << ": ";
    const auto curStall = stalls.top();
    if ((curStall - 1) % 2 == 0) {
      const auto addStall = (curStall - 1) / 2;
      std::cout << addStall << " " << addStall;
    } else {
      const auto addStall = curStall / 2;
      std::cout << addStall << " " << (addStall - 1);
    }
    std::cout << std::endl;
  }
  return 0;
}
