#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
std::string solve(const std::string &x, int length) {
  std::vector<int> numbers(x.length());
  std::transform(std::begin(x), std::end(x), std::begin(numbers), [](char x) { return x == '+' ? 1 : 0; });

  auto f = std::find(std::begin(numbers), std::end(numbers), 0);
  auto l = std::end(numbers);
  int count = 0;
  while (f != l) {
    if (l - f < length) return "IMPOSSIBLE";
    std::transform(f, f + length, f, [](int x) { return !x; });
    ++f;
    f = std::find(f, std::end(numbers), 0);
    ++count;
  }
  return std::to_string(count);
}

int main() {
  int n, s;
  std::cin >> n;
  std::string buffer;
  for (int i = 0; i < n; ++i) {
    std::cin >> buffer >> s;
    std::cout << "Case #" << i + 1 << ": " << solve(buffer, s) << std::endl;
  }
  return 0;
}
