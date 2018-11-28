// 55724827 Gerardo
#include <iostream>
#include <string.h>

using namespace std;
int T;
char N[30];

int main() {
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> N;
    int nlen = strlen(N);
    cout << "Case #" << t+1 << ": ";
    if (nlen > 1) {
      for (int i = nlen-2; i >= 0; i--) {
        if (N[i] > N[i+1]) {
          // Decrease N[i]
          int k = 0;
          while (N[i-k] == '0') {
            N[i-k] = '9';
          }
          N[i-k]--;
          // Everyone to the right is 9
          k = 0;
          do {
            N[i+1+k] = '9';
            k++;
          } while(i+1+k < nlen && N[i+1+k] != '9');
        }
      }
      bool flag = true;
      for (int i = 0; i < nlen; i++) {
        if (flag && N[i]=='0') {
          continue;
        }
        flag = false;
        cout << N[i];
      }
      cout << endl;
    } else {
      cout << N << endl;
    }
  }
  return 0;
}

//     cout << "Case #" << t+1 << ": ";
/*

4
132
1000
7
111111111111111110


1000000000000000000

*/
