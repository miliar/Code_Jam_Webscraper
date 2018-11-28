#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <map>

std::pair<size_t, size_t> split(size_t n) {
  auto low = (n - 1) / 2;
  auto high = n - 1 - low;
  return {high, low};
}

std::pair<size_t, size_t> solve(size_t N, size_t K) {
  std::map<uint64_t, uint64_t> space;
  space[N] = 1;

  while (true) {
    auto p = *space.rbegin();
    auto s = split(p.first);
    if (K <= p.second) return s;
    K -= p.second;

    space.erase(p.first);
    space[s.first] += p.second;
    space[s.second] += p.second;
  }
}

int main() {
  std::cout.setf(std::ios::unitbuf);  // unbuffered output

  uint64_t numberOfTestcases;
  std::cin >> numberOfTestcases;
  for (size_t i = 1; i <= numberOfTestcases; ++i) {
    size_t N, K;
    std::cin >> N >> K;
    auto r = solve(N, K);
    std::cout << "Case #" << i << ": " << r.first << " " << r.second << "\n";
  }
  return 0;
}
