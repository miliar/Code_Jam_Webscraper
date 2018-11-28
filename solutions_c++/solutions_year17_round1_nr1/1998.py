#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


#define LL long long


extern void solve(int R, int C);

int main() {
  int T;
  cin >> T;
  cerr << "T: " << T << endl;

  for (int i = 1; i <= T; i++) {
    int R, C;
    cin >> R >> C;
    cout << "Case #" << i << ":" << endl;
    solve(R, C);
  }
  return 0;
};

void debug(int R, int C, char A[30][30]) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
//      cout << A[i][j];
    }
//    cout << endl;
  }
//  cout << endl;
}

void solve(int R, int C) {
  char A[30][30];
  for (int i = 0; i < 30; i++)
  for (int j = 0; j < 30; j++) {
    A[i][j] = '?';
  }
  
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      char c; cin >> c;
      A[i][j] = c;
    }
  }
  
  debug(R, C, A);
  
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (A[i][j] != '?') {
        for (int k = j - 1; k >= 0; k--) {
          if (A[i][k] == '?') A[i][k] = A[i][j];
          else break;
        }
        for (int k = j + 1; k < C; k++) {
          if (A[i][k] == '?') A[i][k] = A[i][j];
          else break;
        }
      }
    }
  }
  
  debug(R, C, A);

  for (int j = 0; j < C; j++) {
    for (int i = 0; i < R; i++) {
      if (A[i][j] != '?') {
        for (int k = i - 1; k >= 0; k--) {
          if (A[k][j] == '?') A[k][j] = A[i][j];
          else break;
        }
        for (int k = i + 1; k < R; k++) {
          if (A[k][j] == '?') A[k][j] = A[i][j];
          else break;
        }
      }
    }
  }
  debug(R, C, A);

  
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cout << A[i][j];
    }
    cout << endl;
  }
}
