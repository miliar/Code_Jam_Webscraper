#include <cstdint>

#include <algorithm>
#include <iostream>
#include <vector>


namespace {

std::int64_t Solve(std::int64_t N) {
  std::vector<int> digits;
  while (N) {
    digits.push_back(N % 10);
    N /= 10;
  }
  std::reverse(digits.begin(), digits.end());
  int first_decreasing = -1;
  for (int i = 1; i < digits.size(); ++i) {
    if (digits[i] < digits[i - 1]) {
      first_decreasing = i;
      break;
    }
  }
  if (first_decreasing > 0) {
    for (int i = first_decreasing; i < digits.size(); ++i) {
      digits[i] = 9;
    }
    --digits[first_decreasing - 1];
    for (int i = first_decreasing - 1; i > 0; --i) {
      if (digits[i] >= digits[i - 1]) break;
      digits[i] = 9;
      --digits[i - 1];
    }
  }
  for (int d : digits) {
    N = N * 10 + d;
  }
  return N;
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    std::int64_t N;
    std::cin >> N;
    std::cout << "Case #" << i << ": " << Solve(N) << std::endl;
  }

  return 0;
}
