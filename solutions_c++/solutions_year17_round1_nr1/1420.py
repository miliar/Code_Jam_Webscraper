#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
  int T, R, C, t = 1;
  char cake[25][25];

  cin >> T;
  while (T--) {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        cin >> cake[i][j];
      }
    }

    bool swap = false;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        swap = false;
        if (cake[i][j] == '?') {
          if (i-1 >= 0) {
            if (cake[i-1][j] != '?') {
              cake[i][j] = cake[i-1][j];
              swap = true;
            }
          }
          if (i+1 < R) {
            if (cake[i+1][j] != '?') {
              cake[i][j] = cake[i+1][j];
              swap = true;
            }
          }
        }
        if (swap) {
          i = -1;
          j = C;
          break;
        }
      }
    }

    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        swap = false;
        if (cake[i][j] == '?') {
          if (j-1 >= 0) {
            if (cake[i][j-1] != '?') {
              cake[i][j] = cake[i][j-1];
              swap = true;
            }
            }
          if (j+1 < C) {
            if (cake[i][j+1] != '?') {
              cake[i][j] = cake[i][j+1];
              swap = true;
            }
            }
        }
        if (swap) {
          i = -1;
          j = C;
          break;
        }
      }
    }


    cout << "Case #" << t << ":" << endl;
    t++;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j)
        cout << cake[i][j];
      cout << endl;
    }
  }

  return 0;
}
