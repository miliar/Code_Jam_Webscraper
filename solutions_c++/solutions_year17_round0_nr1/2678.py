#include <iostream>

int main() {

  std::ios_base::sync_with_stdio(false);

  int t, totalCases;
  std::cin >> t;
  totalCases = t;

  while (t--) {
    std::string stringForLeft, stringForRight;
    int k, startFromLeft = 0, startFromRight = 0;

    std::cin >> stringForLeft >> k;

    stringForRight = stringForLeft;

    std::cout << "Case #" << totalCases - t << ": ";
    for (int i = 0; i <= stringForLeft.size() - k; i++) {
      if (stringForLeft[i] == '-') {
        startFromLeft++;
        for (int j = i; j <= i + k - 1; j++) {
          if (stringForLeft[j] == '-') {
            stringForLeft[j] = '+';
          } else if (stringForLeft[j] == '+') {
            stringForLeft[j] = '-';
          }
        }
      }
    }

    if (stringForLeft.find('-') == std::string::npos) {
      for (int i = stringForRight.size() - 1; i >= k - 1; i--) {
        if (stringForRight[i] == '-') {
          startFromRight++;
          for (int j = i; j >= i - k + 1; j--) {
            if (stringForRight[j] == '-') {
              stringForRight[j] = '+';
            } else if (stringForRight[j] == '+') {
              stringForRight[j] = '-';
            }
          }
        }
      }
      if (stringForRight.find('-') == std::string::npos) {
        std::cout << std::min(startFromLeft, startFromRight) << '\n';
      } else {
        std::cout << "IMPOSSIBLE\n";
      }
    } else {
      std::cout << "IMPOSSIBLE\n";
    }
  }

  return 0;
}