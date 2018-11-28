#include <iostream>
using namespace std;
int main() {
  int t, r, c;
  char q;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cin >> r >> c;
    char m[r][c];
    bool e[r];
    for(int i = 0; i < r; i++) {
      char last = '?';
      int distinct = 0;
      for(int j = 0; j < c; j++) {
        cin >> m[i][j];
        if(m[i][j] == '?') {
          m[i][j] = last;
        }
        else {
          distinct++;
          if(distinct == 1) {
            for(int k = 0; k < j; k++) {
              m[i][k] = m[i][j];
            }
          }
          last = m[i][j];
        }
      }
      // propaga sopra e sotto
      if(distinct == 0) {
        e[i] = true;
      }
      else {
        e[i] = false;
      }
    }
    bool first = true;
    int last = 0;
    for(int i = 0; i < r; i++) {
      if(!e[i]) {
        if(first)
        for(int j = 0; j < i; j++) {
          for(int k = 0; k < c; k++) {
            m[j][k] = m[i][k];
          }
        }
        first = false;
        last = i;
      }
      else if(e[i]) {
        for(int k = 0; k < c; k++) {
          m[i][k] = m[last][k];
        }
      }

    }

    printf("Case #%d:\n", tc);
    for(int i = 0; i < r; i++) {
      for(int j = 0; j < c; j++) {
        cout << m[i][j];
      }
      cout << '\n';
    }

  }
}
