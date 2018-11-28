// 55724827 Gerardo
#include <iostream>
#include <string.h>

using namespace std;

int main() {
  int T, K;
  char S[1010];
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> S >> K;
    int cont = 0;
    int slen = strlen(S) - (K-1);
    for (int s = 0; s < slen; s++) {
      if (S[s] == '-') {
        cont++;
        for (int k = 0; k < K; k++) {
          if (S[s+k] == '-') {
            S[s+k] = '+';
          } else {
            S[s+k] = '-';
          }
        }
      }
    }
    slen = strlen(S);
    bool impossible = false;
    for (int k = 1; k < K; k++) {
      if (S[slen-k] == '-') {
        impossible = true;
        break;
      }
    }
    cout << "Case #" << t+1 << ": ";
    if (impossible) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << cont << endl;
    }
  }
  return 0;
}


/*

3
---+-++- 3
+++++ 4
-+-+- 4


*/
