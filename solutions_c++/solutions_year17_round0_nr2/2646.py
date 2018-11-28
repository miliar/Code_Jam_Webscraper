#include <algorithm>
#include <iostream>
#include <vector>

bool isUseful(std::vector<int> &v) {
  for (auto i = 0; i <= v.size() - 2; i++) {
    if (v[i] > v[i + 1]) {
      v[i]--;
      for (auto j = i + 1; j < v.size(); j++) {
        v[j] = 9;
      }
      return false;
    }
  }
  return true;
}

void printVec(const std::vector<int> &vec) {

  auto startFrom = std::find_if_not(
      vec.begin(), vec.end(), [](int currentVal) { return currentVal == 0; });

  for (auto current = startFrom; current != vec.end(); current++) {
    std::cout << *current;
  }
  std::cout << '\n';
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int t, totalCases;
  std::cin >> t;
  totalCases = t;

  while (t--) {
    long long int n;
    std::cin >> n;

    std::vector<int> number;
    while (n > 0) {
      auto temp = n % 10;
      number.insert(number.begin(), temp);
      n = n / 10;
    }
    // std::cout << " number is: " << '\n';
    // printVec(number);

    if (number.size() > 1) {
      while (!isUseful(number))
        ;
    }

    std::cout << "Case #" << totalCases - t << ": ";
    printVec(number);
  }

  return 0;
}