#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

void dumpTest(const std::vector<bool> &test) {
  for (auto b: test) {
    if (b) {
      std::cout << "h ";
    } else {
      std::cout << "s ";
    }
  }
  std::cout << std::endl;
}

bool doTestCase(std::vector<bool> test, int spatula, int &result) {
  if (test.size() == 0) {
    result = 0;
    return true;
  }

  if (spatula > test.size()) {
    for (int i = 0; i < test.size(); i++) {
      if (!test[i]) {
        return false;
      }
    }
    return true;
  }

  result = 0;
  for (int i = 0; i < test.size() - spatula + 1; ++i) {
    if (!test[i]) {
      ++result;
      for (int j = 0; j < spatula; ++j) {
        test[i + j] = !test[i + j];
      }
    }
    // dumpTest(test);
  }

  for (int i = 0; i < test.size(); ++i) {
    if (!test[i]) {
      return false;
    }
  }
  return true;
}

int main() {
  int num_cases = 0;
  std::cin >> num_cases;
  for (int i = 0; i < num_cases; ++i) {
    std::string test_case;
    int spatula = 0;

    std::cin >> test_case;
    std::cin >> spatula;

    std::vector<bool> test_case_bool;
    for (auto c: test_case) {
      if (c == '-')
        test_case_bool.push_back(false);
      else if (c == '+')
        test_case_bool.push_back(true);
      else
        std::cerr << "parsing failed" << std::endl;
    }

    int result = -1;
    auto success = doTestCase(test_case_bool, spatula, result);

    std::cout << "Case #" << i + 1 << ": ";
    if (success) {
      std::cout << result;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
  return 0;
}
