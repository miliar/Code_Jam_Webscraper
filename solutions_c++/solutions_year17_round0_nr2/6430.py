#include <algorithm>
#include <iostream>
#include <vector>

std::vector<uint64_t> extract_digits(uint64_t x) {
  std::vector<uint64_t> digits;
  digits.reserve(10);
  digits.push_back(x % 10);
  x = x / 10;
  while (x != 0) {
    digits.push_back(x % 10);
    x = x / 10;
  }
  std::reverse(std::begin(digits), std::end(digits));
  return digits;
}

void solve(uint64_t x) {
  auto digits = extract_digits(x);
  auto f = std::begin(digits);
  auto l = std::end(digits);

  while(true) {
    auto p = std::adjacent_find(f, l, [](auto x, auto y) { return y < x; });
    if (p == l) break;
    --(*p);
    *(p + 1) = 9;
    std::fill(p + 1, l, 9);
  }
  while(*f == 0) ++f;
  std::for_each(f, std::end(digits), [](auto x) { std::cout << x; });
  std::cout << std::endl;;
}

int main() {
  uint64_t n, x;
  std::cin >> n;
  for (int i = 1; i <= n; ++i) {
    std::cin >> x;
    std::cout << "Case #" << i << ": ";
    solve(x);
  } 
}
