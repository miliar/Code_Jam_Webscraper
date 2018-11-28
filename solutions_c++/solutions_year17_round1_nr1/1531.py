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
    int R, C;
    cin >> R >> C;
    char S[30][30];

    for (int i = 0; i < R; ++i)
    {
      for (int j = 0; j < C; ++j)
      {
        cin >> S[i][j];
      }
    }

    // col
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j)
      {
        if (S[i][j] == '?') {
          int k = j + 1;
          for (; (k < C) && (S[i][k] == '?'); ++k);

          char cc = S[i][k];

          if (k == C)
            if (j == 0)
              continue;
            else
              cc = S[i][j - 1];
          
          for (int l = j; l <= k; ++l) {
            S[i][l] = cc;
          }
        }
      }
    }

    for (int j = 0; j < C; ++j) {
      for (int i= 0; i < R; ++i)
      {
        if (S[i][j] == '?') {
          int k = i + 1;
          for (; (k< R) && (S[k][j] == '?'); ++k);

          char cc;

          if (k == R)
            if (i == 0)
              continue;
            else
              cc = S[i-1][j];
          else
            cc = S[k][j];

          for (int l = i; l <= k; ++l) {
            S[l][j] = cc;
          }
        }
      }
    }

    cout << "Case #" << t + 1 << ":" << endl;


    for (int i = 0; i < R; ++i)
    {
      for (int j = 0; j < C; ++j)
      {
        cout << S[i][j];
      }
      if (i < R-1)
        cout << endl;
    }


    cout << endl;
  }

  return 0;
}