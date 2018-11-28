#include <iostream>
#include <string>

using namespace std;

int main() {
  string S;
  int T, K;
  cin >> T;
  for (int t = 1 ; t <= T; t++) {
    cin >> S >> K;
    int A = 0;
    for (int i = 0; i < S.length() - K + 1; i++) {
      if (S[i] == '-') {
        for (int j = 0; j < K; j++)
          S[i + j] = S[i + j] == '-' ? '+' : '-';
          A++;
      }
    }
    for (int i = 0; i < S.length(); i++) {
      if (S[i] == '-') {
        A = -1;
      }
    }
    printf("Case #%d: %s\n", t, A == -1 ? "IMPOSSIBLE" : to_string(A).c_str());
  }
  return 0;
}