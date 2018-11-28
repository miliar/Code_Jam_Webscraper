#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    string S;
    int K;
    cin >> S >> K;
    int ans = 0;
    for (int i = 0; i <= S.size() - K; ++i) {
      if (S[i] == '+') {
        continue;
      }
      ++ans;
      for (int j = 0; j < K; ++j) {
        S[i + j] = S[i + j] == '-' ? '+' : '-';
      }
    }
    for (int i = 0; i < S.size(); ++i) {
      if (S[i] != '+') {
        ans = -1;
      }
    }
    if (ans != -1) {
      printf("Case #%d: %d\n", cases + 1, ans);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", cases + 1);
    }
  }
}