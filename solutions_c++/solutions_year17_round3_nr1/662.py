#include <iostream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <iomanip>

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_number = 0; test_number < number_of_tests; ++test_number) {
    int k, n;
    std::cin >> n >> k;
    std::vector<std::pair<long long, long long>> pancakes(n);
    for (auto& pancake : pancakes) {
      std::cin >> pancake.first >> pancake.second;
    }
    std::sort(pancakes.begin(), pancakes.end());
    long long max_result = 0;
    for (int i = 0; i < pancakes.size(); ++i) {
      std::sort(pancakes.begin(), pancakes.begin() + i, 
          [](const auto& a, const auto& b) {
            return a.first * a.second < b.first * b.second;
          });
      long long sum = 0;
      for (int j = std::max(i - k + 1, 0); j <= i; ++j) {
        sum += pancakes[j].first * pancakes[j].second;
      }
      long long current_result = 2 * sum + pancakes[i].first * pancakes[i].first;
      max_result = std::max(max_result, current_result);
    }
    std::cout << "Case #" << test_number + 1 << ": " << std::fixed <<
      std::setprecision(20) << max_result * M_PI << std::endl;
  }

  return 0;
}
