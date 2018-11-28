#include <iostream>
#include <string>


using namespace std;
int main() {
  int t;
  cin >> t;

  for (int test=1;test<=t;test++) {
    cout << "Case #" << test << ":" << endl;
    int r, c;
    cin >> r >> c;
    char cake[r][c];
    for(int i=0;i<r;i++)
      for (int j=0;j<c;j++)
        cin >> cake[i][j];

    for(int i=0;i<r;i++) {
      char mark = '-';
      for (int j=0;j<c;j++) {
        if (cake[i][j] != '?') {
          if (mark == '-') {
            int k = j-1;
            while (k>=0 && cake[i][k]=='?') {
              cake[i][k] = cake[i][j];
              k--;
            }
          }
          mark = cake[i][j];
        }
        else {
          if (mark != '-') cake[i][j] = mark;
        }
      }
    }

    for(int j=0;j<c;j++) {
      char mark = '-';
      for (int i=0;i<r;i++) {
        if (cake[i][j] != '?') {
          if (mark == '-') {
            int k = i-1;
            while (k>=0 && cake[k][j]=='?') {
              cake[k][j] = cake[i][j];
              k--;
            }
          }
          mark = cake[i][j];
        }
        else {
          if (mark != '-') cake[i][j] = mark;
        }
      }
    }

    for(int i=0;i<r;i++) {
      for (int j=0;j<c;j++) {
        cout << cake[i][j];
      }
      cout << endl;
    }
  }

  return 0;
}