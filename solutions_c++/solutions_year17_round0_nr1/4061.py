#include <string>
#include <iostream>
using namespace std;

int main() {
  int N, K;
  string S;
  cin >> N;
  for (int i = 1; i <= N; ++i) {
    cin >> S >> K;
    int ans = 0;
    for (int j = 0; j < S.length() - K + 1; ++j) {
      if (S[j] == '-') {
        ans++;
        for (int k = j; k < j + K; ++k)  {
          if (S[k] == '-') {
            S[k] = '+';
          } else {
            S[k] = '-';
          }
        }
      }
    }
    for (int j = 0; j < S.length(); ++j) {
      if (S[j] == '-') {
        ans = -1;
        break;
      }
    }
    cout << "Case #" << i << ": ";
    if (ans == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << ans;
    }
    cout << "\n";
  }
  return 0;
}
