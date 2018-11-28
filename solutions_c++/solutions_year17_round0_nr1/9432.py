#include <iostream>
#include <string>

using namespace std;

int main() {
  freopen("input.in", "r", stdin);
  freopen("output.out", "w", stdout);

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    char S[1005];
    int K;
    cin >> S >> K;
    int result = 0;
    int n = strlen(S);
    bool impossible = false;

    for (int i = 0; i < n; i++) {
      if (S[i] == '+') {
        continue;
      } else if (i + K > n) {
        impossible = true;
        break;
      } else {
        result += 1;
        for (int j = i; j < i + K; j++) {
          if (S[j] == '+') {
            S[j] = '-';
          } else {
            S[j] = '+';
          }
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (impossible) {
      cout << "IMPOSSIBLE";
    } else {
      cout << result;
    }
    cout << endl;
  }
  return 0;
}
