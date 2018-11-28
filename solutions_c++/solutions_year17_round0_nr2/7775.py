#include <bits/stdc++.h>
int main() {
  std::string S;
  int T;
  std::cin >> T;
  for (int t = 0; t < T; t++) {
    std::cin >> S;
    std::string ans = S;
    int i = 0;
    while (i < S.size()-1 && S[i] <= S[i+1]) i++;
    if (i != S.size()-1) {
      if (S[i] == '1') {
        ans = std::string(S.size()-1, '9');
      } else {
        while (i > 0 && S[i] == S[i-1]) i--;
        ans[i]--;
        i++;
        while (i < S.size()) {
          ans[i] = '9';
          i++;
        }
      }
    }
    //int N = std::atoi(S.c_str());
    //int ans_int = 1;
    //for (int i = 0; i <= N; i++) {
    //  auto i_str = std::to_string(i);
    //  bool good = true;
    //  for (int j = 0; j < i_str.size()-1; j++) {
    //    if (i_str[j] > i_str[j+1]) {
    //      good = false;
    //      break;
    //    }
    //  }
    //  if (good) ans_int = i;
    //}
    std::cout << "Case #" << t+1 << ": " << ans << std::endl;
  }
  return 0;
}
