#include<iostream>
#include<string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    string S;
    int K;
    cin >> S >> K;
    int flips = 0;
    for (int i = 0; i <= S.size() - K; ++i) {
      if (S[i] == '-') {
        ++flips;
        for (int j = 0; j < K; ++j) {
          S[i+j] ^= ('+'^'-');
        }
      }
    }
    bool possible = true;
    for (int i = S.size() - K; possible and i < S.size(); ++i) {
      possible = S[i] == '+';
    }
    cout << "Case #" << cas << ": ";
    if (possible) cout << flips;
    else cout << "IMPOSSIBLE";
    cout << endl;
  }
}
