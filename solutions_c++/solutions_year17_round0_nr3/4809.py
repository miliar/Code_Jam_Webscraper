#include <iostream>
#include <map>
#include <tuple>

std::tuple<uint64_t, uint64_t> findLR(uint64_t n, uint64_t k) {
  std::map<uint64_t, uint64_t> cuts = {{n, 1}};
  while (!cuts.empty()) {
    uint64_t cutSize;
    uint64_t cutCounter;
    std::tie(cutSize, cutCounter) = *cuts.rbegin();
    cuts.erase(cutSize);
    const uint64_t lSize = cutSize / 2;
    const uint64_t rSize = (cutSize - 1) / 2;
    if (k <= cutCounter) {
      return std::make_tuple(lSize, rSize);
    }
    k -= cutCounter;
    if (lSize > 0) {
      cuts[lSize] += cutCounter;
    }
    if (rSize > 0) {
      cuts[rSize] += cutCounter;
    }
  }
  throw std::logic_error("Unable to spread all people.");
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    uint64_t n, k;
    std::cin >> n >> k;
    uint64_t lSize, rSize;
    std::tie(lSize, rSize) = findLR(n, k);
    std::cout << "Case #" << caseNo + 1 << ": " << lSize << ' ' << rSize
              << '\n';
  }
  return 0;
}
