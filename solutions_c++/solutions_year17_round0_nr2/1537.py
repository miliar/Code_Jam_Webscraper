#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    char N[100] = {};
    char E[100] = {};
    cin >> N;

    // Check tidy
    int l = strlen(N);

    bool isTidy = true;
    for (int i = l - 1; i > 0; --i) {
      if (N[i] < N[i - 1]) {
        isTidy = false;
        break;
      }
    }

    if (!isTidy) {
      for (int i = l - 1; i > 0; --i) {
        if (N[i] < N[i - 1]) {
          for (int j = i; j < l; ++j)
            E[j] = '9';
          N[i-1] = N[i-1] - 1;
        }
        else {
          E[i] = N[i];
        }
      }
      E[0] = N[0];
    }


    cout << "Case #" << t + 1 << ": ";

    // Result
    if (isTidy) {
      cout << N;
    }
    else {
      if (E[0] > '0') {
        cout << E;
      }
      else {
        for (int i = 1; i < l; ++i)
          cout << E[i];
      }
    }

    cout << endl;
  }

  return 0;
}