#include <iostream>
#include <string>
#include <vector>

std::vector<bool> readSequence(std::istream* istream) {
  std::string buffer;
  *istream >> buffer;
  std::vector<bool> result;
  result.reserve(buffer.size());
  for (char c : buffer) {
    result.push_back(c == '+');
  }
  return result;
}

int findNumberOfFlips(const std::vector<bool>& sequence, size_t flipWith) {
  int result = 0;
  bool neutral = true;
  std::vector<bool> flops(sequence.size(), false);
  for (size_t i = 0; i < sequence.size(); ++i) {
    if (sequence.at(i) != neutral) {
      if (i + flipWith > sequence.size()) {
        return -1;
      }
      result += 1;
      neutral = !neutral;
      flops.at(i + flipWith - 1) = true;
    }
    if (flops.at(i)) {
      neutral = !neutral;
    }
  }
  return result;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    const auto sequence = readSequence(&std::cin);
    size_t flipWidth;
    std::cin >> flipWidth;
    const auto numberOfFlips = findNumberOfFlips(sequence, flipWidth);
    std::cout << "Case #" << caseNo + 1 << ": ";
    if (numberOfFlips < 0) {
      std::cout << "IMPOSSIBLE";
    } else {
      std::cout << numberOfFlips;
    }
    std::cout << '\n';
  }
  return 0;
}
