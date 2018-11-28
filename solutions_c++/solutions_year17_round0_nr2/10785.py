#include <algorithm>
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

auto allElements(unsigned i) {
  std::vector<decltype(i)> returned;
  while (i > 0) {
    returned.push_back(i % 10);
    i = static_cast<decltype(i)>(i / 10);
  }
  return returned;
}

bool isTidy(unsigned i) {
  auto numbers = allElements(i);
  std::reverse(numbers.begin(), numbers.end());
  for (auto i = 1u; i < numbers.size(); ++i) {
    if (numbers[i - 1] > numbers[i]) return false;
  }

  return true;
}

int main() {
  int T;
  cin >> T;
  for (auto i = 0; i < T; ++i) {
    unsigned N;
    cin >> N;
    for (auto j = N; j > 0; --j) {
      if (isTidy(j)) {
        cout << "Case #" << i + 1 << ": " << j << endl;
        break;
      }
    }
  }
}

// g++ -Wall -Wextra -pedantic -o3 -o main.exe  source.cpp