#include <array>
#include <iostream>
#include <string>

uint64_t findMaxTidyNumber(uint64_t limit) {
  const auto limitStr = std::to_string(limit);
  uint64_t limitPrefix = 0;
  std::array<uint64_t, 10> frontier = {{}};
  for (char c : std::to_string(limit)) {
    limitPrefix = 10 * limitPrefix + (c - '0');
    std::array<uint64_t, 10> nextFrontier = {{}};
    for (size_t i = 0; i < nextFrontier.size(); ++i) {
      for (size_t j = 0; j <= i; ++j) {
        auto x = 10 * frontier.at(j) + i;
        if (nextFrontier.at(i) < x && x <= limitPrefix) {
          nextFrontier.at(i) = x;
        }
      }
    }
    frontier = nextFrontier;
  }
  uint64_t result = 0;
  for (auto x : frontier) {
    result = std::max(result, x);
  }
  return result;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    uint64_t limit;
    std::cin >> limit;
    std::cout << "Case #" << caseNo + 1 << ": " << findMaxTidyNumber(limit)
              << '\n';
  }
  return 0;
}
