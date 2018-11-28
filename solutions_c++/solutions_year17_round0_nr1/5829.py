#include <iostream>
#include <vector>
#include <string>

using namespace std;
std::string pancake(std::string S, int K);

int main() {
  int t, K;
  string S;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> S >> K;
    string result = pancake(S, K);
    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}

std::string pancake(std::string S, int K) {
  int numFlips = 0;
  for (int i = 0; i < S.length(); i++) {
    if (S[i] == '-') {
      if (i + K > S.length())
        return "IMPOSSIBLE";
      // cout << "HERE" << i << endl;
      for (int j = i; j < i+K; j++ ) {
        S[j] = (S[j] == '-') ? '+' : '-';
      }
      ++numFlips;
    }
    // cout << i << ": " << S << endl;
  }
  return std::to_string(numFlips);
}
