#include <iostream>
#include <vector>
#include <algorithm>

const long long inf = 1e9;

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_number = 0; test_number < number_of_tests; ++test_number) {
    int a_c, a_j;
    std::cin >> a_c >> a_j;
    std::vector<std::pair<long long, long long>> cameron(a_c), jamie(a_j);
    for (auto& pr : cameron) {
      std::cin >> pr.first >> pr.second;
    }
    for (auto& pr : jamie) {
      std::cin >> pr.first >> pr.second;
    }
    std::sort(cameron.begin(), cameron.end());
    std::sort(jamie.begin(), jamie.end());
    long long result = inf;
    for (int first = 0; first < 2; ++first) {
      std::vector<std::vector<long long>> dp(2,
          std::vector<long long>(24 * 60 + 1, inf));
      dp[first][0] = 0;
      int current_cameron = 0, current_jamie = 0;
      for (int i = 1; i <= 24 * 60; ++i) {
        while (current_cameron < cameron.size() &&
            cameron[current_cameron].second < i) {
          current_cameron++;
        }
        while (current_jamie < jamie.size() &&
            jamie[current_jamie].second < i) {
          current_jamie++;
        }
        bool cameron_active = true, jamie_active = true;
        if (current_cameron < cameron.size() &&
            cameron[current_cameron].first < i) {
          cameron_active = false;
        }
        if (current_jamie < jamie.size() && jamie[current_jamie].first < i) {
          jamie_active = false;
        }
        for (int j = 24 * 60; j >= 0; --j) {
          if (jamie_active) {
            dp[1][j] = std::min(dp[1][j], dp[0][j] + 1);
          } else {
            dp[1][j] = inf;
          }
          if (cameron_active && j > 0) {
            dp[0][j] = std::min(dp[1][j - 1] + 1, dp[0][j - 1]);
          } else {
            dp[0][j] = inf;
          }
        }
      }
      //if (first == 0 && test_number == 1) {
        //for (int i = 0; i <= 24 * 60; ++i) {
          //std::cout << i << ": " << dp[first][i] << std::endl;
        //}
      //}
      result = std::min(result, dp[first][12 * 60]);
    }
    std::cout << "Case #" << test_number + 1 << ": " << result << std::endl;
  }
  return 0;
}
