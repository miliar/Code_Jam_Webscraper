#include <iostream>
#include <vector>

#include <cstdint>

void dumpDigits(const std::vector<int> &digits) {
  for (auto d: digits) {
    std::cout << d << " ";
  }
  std::cout << std::endl;
}

bool isTidy(const std::vector<int> &digits) {
  int last = 0;
  for (auto d: digits) {
    if (d < last) {
      return false;
    }
    last = d;
  }
  return true;
}

// MSB first
std::vector<int> toDigits(uint64_t input) {
  std::vector<int> ret;
  while (input) {
    ret.insert(ret.begin(), input % 10);
    input /= 10;
  }
  return ret;
}

uint64_t toInt(const std::vector<int> &digits) {
  uint64_t ret = 0;
  for (auto d: digits) {
    ret = 10*ret + d;
  }
  return ret;
}

uint64_t tidy(uint64_t input) {
  std::vector<int> digits = toDigits(input);
  // std::cerr << "start" << std::endl;
  // dumpDigits(digits);
  while (!isTidy(digits)) {
    // find the first place where the number isn't tidy,
    // decrement by one and set all the ones after to 9
    int last = digits[0];
    int i = 1;
    while (digits[i] >= last) {
      last = digits[i];
      ++i;
    }

    const int to9 = i;
    // go back 1 to decrement the prefix
    --i;

    digits[i]--;
    while (digits[i] == -1) {
      digits[i] = 9;

      --i;
      --digits[i];
    }

    for (int j = to9; j < digits.size(); ++j) {
      digits[j] = 9;
    }
    // std::cerr << "modified" << std::endl;
    // dumpDigits(digits);
  }

  return toInt(digits);
}

int main() {
  int numCases = 0;
  std::cin >> numCases;

  for (int i = 0; i < numCases; ++i) {
    uint64_t input = 0;
    std::cin >> input;

    uint64_t output = tidy(input);
    std::cout << "Case #" << i + 1 << ": " << output << std::endl;
  }
}
