#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    string n;
    cin >> n;

    std::cout << "Case #" << i + 1 << ": ";

    for (int j = 0; j < n.size(); ++j) {
      bool ok = true;
      for (int k = j + 1; k < n.size(); ++k) {
        if (n[j] < n[k])
          break;
        if (n[k] < n[j]) {
          ok = false;
          break;
        }
      }
      if (ok) {
        std::cout << n[j];
        continue;
      }

      if (n[j] > '1')
        std::cout << (char)(n[j] - 1);

      for (int k = j + 1; k < n.size(); ++k)
        std::cout << 9;

      break;
    }

    std::cout << std::endl;
  }

  return 0;
}
