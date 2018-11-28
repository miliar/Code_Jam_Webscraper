#include <iostream>
#include <string>
#include <algorithm>

int main()
{
  int T;
  std::cin >> T;
  for (int i = 0; i < T; i++) {
    int cnt = 0;
    std::string str;
    int K;
    std::cin >> str >> K;
    for (int j = 0; j < str.size() - K + 1; j++) {
      if (str[j] == '-') {
        for (int k = 0; k < K; k++) {
          str[j + k] = str[j + k] == '-' ? '+' : '-';
        }
        cnt++;
      }
    }
    std::cout << "Case #" << i + 1 << ": ";
    if (std::all_of(str.begin(), str.end(), [](char c)
                    {return c == '+';})) {
      std::cout << cnt << std::endl;
    } else {
      std::cout << "IMPOSSIBLE" << std::endl;
    }
  }
  return 0;
}
