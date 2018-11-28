#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <set>

size_t areDigitsSorted(size_t a) {
  size_t prevDigit = 10;
  size_t curDigit = 0;
  size_t factor = 1;
  size_t minuend = 0;
  while (true) {
    curDigit = a % 10;
    // right to left
    if (curDigit > prevDigit) return minuend + 1;
    prevDigit = curDigit;
    minuend += curDigit * factor;
    factor *= 10;

    if (a < 10) break;
    a /= 10;
  }
  return 0;
}

size_t solve(size_t N) {
  while (N > 0) {
    size_t factor = areDigitsSorted(N);
    if (!factor) return N;
    std::cerr << "Using factor " << factor << " from " << N << "to "
              << N - factor << "\n";
    N -= factor;
  }
  // precodnition: N >= 1
  assert(false);
}

int main() {
  std::cout.setf(std::ios::unitbuf);  // unbuffered output

  uint64_t numberOfTestcases;
  std::cin >> numberOfTestcases;
  for (size_t i = 1; i <= numberOfTestcases; ++i) {
    size_t N;
    std::cin >> N;
    std::cout << "Case #" << i << ": " << solve(N) << "\n";
  }
  return 0;
}
