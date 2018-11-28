#include <iostream>
#include <sstream>
#include <string>

using namespace std;

// Find first tidy
int num_flips(string S, int K) {
  int num_flips = 0;
  for (int i = 0; i <= S.size() - K; i++) {
    if (S[i] == '-') {
      num_flips++;
      for (int j = 0; j < K; j++) {
        if (S[i + j] == '-') {
          S[i + j] = '+';
        } else if (S[i + j] == '+') {
          S[i + j] = '-';
        }
      }
    }
  }
  int all = true;
  for (int i = S.size() - K + 1; i < S.size(); i++) {
    all &= (S[i] == '+');
  }

  if (all) {
    return num_flips;
  } else {
    return -1;
  }
}

int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    string S;
    cin >> S;
    int K;
    cin >> K;
    int result = num_flips(S, K);
    if (result >= 0) {
      cout << "Case #" << i + 1 << ": " << result << endl;
    } else {
      cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
  }
}
