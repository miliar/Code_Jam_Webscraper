#include <bits/stdc++.h>
using namespace std;

int main() {
  int T;
  cin >> T;

  for(int i = 0; i < T; i++) {

    string S;
    int K;
    cin >> S >> K;

    int flip = 0;

    for(int k = 0; k <= S.length() - K; k++) {
      if(S[k] == '-') {

        for(int j = k; j < k + K; j++) {
          if(S[j] == '+') S[j] = '-';
          else S[j] = '+';
        }

        flip += 1;

      }

    }

    bool isOk = true;
    for(int k = 0; k < S.length(); k++) {
      if(S[k] == '-')
        isOk = false;
    }
    cout << "Case #" << i + 1 << ": ";
    if(isOk) {
      cout << flip << endl;
    }else {
      cout << "IMPOSSIBLE" << endl;
    }

  }


}
