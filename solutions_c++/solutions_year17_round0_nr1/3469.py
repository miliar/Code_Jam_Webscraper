
#include <iostream>
#include <string>

using namespace std;

static int CalculateNumOfTimes(string S, int K) {
  int res = 0;
  for (size_t i = 0; i < S.size(); ++i) {
    if (S[i] == '-') {
      if (i + K > S.size()) {
        return -1;
      }
      for (int j = 0; j < K; ++j) {
        S[i + j] = S[i + j] == '+' ? '-' : '+';
      }
      res += 1;
    }
  }
  return res;
}

int main() {
  int T = 0;
  string S;
  int K = 0;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> S >> K;
    int res = CalculateNumOfTimes(S, K);
    cout << "Case #" << (i + 1) << ": ";
    if (res < 0) {
      cout << "IMPOSSIBLE" << std::endl;
    } else {
      cout << res << std::endl;
    }
  }
  return 0;
}