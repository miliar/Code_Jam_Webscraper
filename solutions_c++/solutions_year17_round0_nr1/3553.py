#include <iostream>

void flipCakes(std::string s, int k, int c) {
  int l = s.length();
  int count = 0;

  for (size_t i = 0; i < l; i++) {
    if(s[i] == '-'){
      if (i+k > l) {
        std::cout << "Case #" << c << ": IMPOSSIBLE" << '\n';
        return;
      }
      count++;
      for (size_t j = i; j < i+k; j++) {
        if (s[j] == '-') {
          s[j] = '+';
        }else{
          s[j] = '-';
        }
      }
    }
  }
  std::cout << "Case #" << c << ": " << count << '\n';
}

int main() {

  int t;
  std::string s;
  int k;
  std::cin >> t;

  for (size_t i = 0; i < t; i++) {
    std::cin >> s;
    std::cin >> k;
    flipCakes(s,k,i+1);
  }

  return 0;
}
