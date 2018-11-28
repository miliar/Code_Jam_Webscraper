/*
Input:
4
132
1000
7
111111111111111110

Output:
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
*/
#include <iostream>

using namespace std;

int
main() {
  int T;

  cin >> T;

  for(int c = 1; c <= T; c++) {
    long N;
    cin >> N;

    int digit[20];
    for(int i = 0; i < 20; i++) {
      digit[i] = 0;
    }

    int n = 0;
    while(N > 0) {
      digit[n] = N % 10;
      N /= 10;
      n++;
    }
    n--;

    bool changed = true;
    while(changed) {
      changed = false;
      for(int i = n; !changed && (i >= 0); i--) {
        if(digit[i] > digit[i-1]) {
          changed = true;
          digit[i]--;
          for(int j = i-1; j >= 0; j--) {
            digit[j] = 9;
          }
        }
      }
    }

    while(digit[n] <= 0) {
      n--;
    }

    cout << "Case #" << c << ": ";
    while(n >= 0) {
      cout << digit[n];
      n--;
    }
    cout << endl;
  }
}
