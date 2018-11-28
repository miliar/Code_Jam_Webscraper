#include <iostream>
#include <string>

int a[1001];
void pnt(int n) {
  for (int i = 0; i < n; i++) std::cout << a[i];
  std::cout << '\n';
}

int main(int argc, char const *argv[]) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; i++) {
    std::string s;
    int n, k;
    std::cin >> s >> k;
    n = s.size();
    for (int j = 0; j < n; j++) a[j] = (s[j] == '+') ? 0 : 1;
    int ways = 0;
    bool possible = true;
    for (int j = 0; j < n; j++) {
      if (a[j] == 0) continue;

      ways ++;
      for (int x = j; x < j + k; x++) {
        if (x == n) {
          possible = false;
          break;
        }
        a[x] = 1 - a[x];
      }
      if (!possible) {
        break;
      }
    }

    if (possible) {
      std::cout << "Case #" << i << ": " << ways << '\n';
    }
    else {
      std::cout << "Case #" << i << ": " << "IMPOSSIBLE" << '\n';
    }
  }
  return 0;
}
