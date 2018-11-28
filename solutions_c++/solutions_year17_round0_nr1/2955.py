#include<bits/stdtr1c++.h>
using namespace std;

int T, K;
string S;

int main() {
  ios::sync_with_stdio(0);
  cin.tie();

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> S >> K;
    int count = 0;
    for (int i = 0; i <= int(S.size() - K); ++i) {
      if (S[i] == '-') {
        count++;
        for (int j = 0; j < K; ++j) {
          if (S[i+j] == '+') {
            S[i+j] = '-';
          } else {
            S[i+j] = '+';
          }
        }
      }
    }
    bool possible = true;
    for (char c : S) {
      possible &= (c == '+');
    }
    cout << "Case #" << t << ": ";
    if (possible) {
      cout << count << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
