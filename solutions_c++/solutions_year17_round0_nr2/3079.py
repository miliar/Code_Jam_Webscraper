#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    string S;
    cin >> S;
    int len = S.size();
    int lastPosistion = S.size() - 1;
    for (int i = S.size() - 1; i >= 1; --i) {
      if (S[lastPosistion] < S[i - 1]) {
        if (S[i - 1] == '0') {
          S[i - 1] = '9';
        } else {
          S[i - 1] -= 1;
        }
        for (int j = i; j <= S.size() - 1; ++j) {
          S[j] = '9';
        }
        lastPosistion = i - 1;
      } else if (S[lastPosistion] > S[i - 1]) {
        lastPosistion = i - 1;
      }
    }
    while (S[0] == '0') {
      S = S.substr(1);
    }
    printf("Case #%d: ", cases + 1);
    cout << S << endl;
  }
}