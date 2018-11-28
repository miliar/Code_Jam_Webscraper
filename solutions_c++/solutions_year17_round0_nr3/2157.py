#include <cstdint>

#include <iostream>
#include <queue>
#include <unordered_map>


namespace {

std::pair<std::int64_t, std::int64_t> Solve(std::int64_t N, std::int64_t K) {
  std::priority_queue<std::int64_t> unoccupied;
  std::unordered_map<std::int64_t, std::int64_t> num_sections;
  unoccupied.push(N);
  num_sections[N] = 1;
  while (true) {
    const std::int64_t length = unoccupied.top();
    unoccupied.pop();
    const std::int64_t shorter = (length - 1) / 2;
    const std::int64_t longer = (length - 1) - shorter;
    if (K <= num_sections[length]) return {longer, shorter};
    K -= num_sections[length];
    if (length > 0) {
      for (const std::int64_t l : {shorter, longer}) {
        if (num_sections.count(l) == 0) unoccupied.push(l);
        num_sections[l] += num_sections[length];
      }
    }
  }
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    std::int64_t N, K;
    std::cin >> N >> K;
    auto result = Solve(N, K);
    std::cout << "Case #" << i << ": "
              << result.first << ' ' << result.second << std::endl;
  }

  return 0;
}
