// 55724827 Gerardo
#include <iostream>
#include <string.h>

using namespace std;
int T, R, C;
char cake[30][30];
int main() {
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> R >> C;
    for (int r = 0; r < R; r++) {
      cin >> cake[r];
    }
    char cur;
    for (int r = 0; r < R; r++) {
      cur = '?';
      for (int c = 0; c < C; c++) {
        if (cake[r][c] != '?') {
          cur = cake[r][c];
          if (c > 0 && cake[r][c-1] == '?') {
            int ite = 1;
            while (c-ite >= 0 && cake[r][c-ite] == '?') {
              cake[r][c-ite] = cur;
              ite++;
            }
          }
        } else {
          cake[r][c] = cur;
        }
      }
    }


    for (int c = 0; c < C; c++) {
      cur = '?';
      for (int r = 0; r < R; r++) {
        if (cake[r][c] != '?') {
          cur = cake[r][c];
          if (r > 0 && cake[r-1][c] == '?') {
            int ite = 1;
            while (r-ite >= 0 && cake[r-ite][c] == '?') {
              cake[r-ite][c] = cur;
              ite++;
            }
          }
        } else {
          cake[r][c] = cur;
        }
      }
    }

    cout << "Case #" << t+1 << ":" << endl;
    for (int r = 0; r < R; r++) {
      cout << cake[r] << endl;
    }

  }
  return 0;
}

/*
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE




Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE



*/
