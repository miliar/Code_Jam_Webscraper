#include <iostream>
#include <string>

int main () {
  int t;
  std::cin >> t;
  for (int j = 1; j <= t; j++) {
    std::string s;
    int k,n,count = 0;
    std::cin >> s >> k;
    n = s.length();
    for (int i = 0; i <= (n-k); i++) {
      if (s[i] == '+') continue;
      count++;
      for (int l = 0; l < k; l++) {
        s[i+l] = s[i+l] == '-' ? '+' : '-';
      }
    }
    int impossible = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '-') impossible = 1;
    }
    std::cout << "Case #" << j << ": ";
    if (impossible) std::cout << "IMPOSSIBLE" << std::endl;
    else std::cout << count << std::endl;
  }
}
