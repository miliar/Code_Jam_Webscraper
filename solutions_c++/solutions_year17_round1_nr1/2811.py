#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool empty[25];
string s[25];
int R,C;

void pre() {
  bool used[27];
  int ii, jj;
  int li, hi, lj, rj,p;
  char c;
  bool check;
  for (int i = 0; i < 27; i++) {
    used[i] = false;
  }

  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (s[i][j] != '?' && !used[s[i][j] - 'A']) {
        c = s[i][j];
        used[c - 'A'] = true;
        li = i;
        hi = i;
        lj = j;
        rj = j;
        for (ii = R - 1; ii>i; ii--) {
          for (jj = 0; jj < C; jj++) {
            if (s[ii][jj] == c) {
              hi = max(hi, ii);
              lj = min(lj, jj);
              rj = max(rj, jj);
            }
          }
        }

        for (p = 1; (li-p >=0) && (lj-p >=0);) {
          check = true;
          ii = li-p;
          for (jj = lj-p; (jj <=rj)&& check;jj++) {
            check = s[ii][jj] == '?';
          }

          jj = lj-p;

          for (ii = li-p; (ii <=hi)&& check;ii++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            li--;
            lj--;
          } else {
            break;
          }
        }

        for (p = 1; (hi+p < R) && (rj+p < C);) {
          check = true;
          ii = hi+p;
          for (jj = lj; (jj <=rj+p)&& check;jj++) {
            check = s[ii][jj] == '?';
          }
          jj = rj+p;
          for (ii = li; (ii <=hi+p)&& check;ii++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            hi++;
            rj++;
          } else {
            break;
          }
        }

        for (ii = li-1; ii>= 0; ii--) {
          check = true;
          for (jj = lj; (jj <= rj) && check; jj++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            li = ii;
          } else {
            break;
          }
        }

        for (ii = hi+1; ii < R; ii++) {
          check = true;
          for (jj = lj; (jj <= rj) && check; jj++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            hi = ii;
          } else {
            break;
          }
        }

        for (jj = lj - 1; jj >= 0; jj--) {
          check = true;
          for (ii = li; (ii <= hi) && check; ii++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            lj = jj;
          } else {
            break;
          }
        }

        for (jj = rj + 1; jj < C; jj++) {
          check = true;
          for (ii = li; (ii <= hi) && check; ii++) {
            check = s[ii][jj] == '?';
          }

          if (check) {
            rj = jj;
          } else {
            break;
          }
        }

        for (ii = li; ii <= hi; ii++) {
          for (jj = lj; jj <= rj; jj++) {
            s[ii][jj] = c;
          }
        }
      }
    }
  }
}
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, i, j, k;
  bool found;
  char c;
  cin >> t;
  for (int _case = 1; _case <= t; _case++) {
      cin >> R >> C;
      for (int i = 0; i < R; i++) {
        cin >> s[i];
      }

      pre();

      /*
      for(i = 0; i < R; i++) {
        for(j = 0; i < C; j++) {
          if (s[i][j] == '?') {

          }
        }
      }
      for(i = 0; i < R; i++) {
        j = 0;
        found = false;
        while (j < C) {
          if (s[i][j] != '?') {
            found = true;
            c = s[i][j];

            for (k = j-1; k >= 0; --k) {
              if (s[i][k] == '?') {
                s[i][k] = s[i][j];
              } else {
                break;
              }
            }

            for (j++; j < C; ++j) {
              if (s[i][j] == '?') {
                s[i][j] = c;
              } else {
                break;
              }
            }
          }
          j++;
        }

        if (found) {
          empty[i] = false;
        } else {
          empty[i] = true;
        }
      }

      for (k = 0; k < R; k++) {
        if (!empty[k]) {
          break;
        }
      }

      for (i = 0; i < k; i++) {
        for (j = 0; j < C; j++) {
          s[i][j] = s[k][j];
        }
      }

      int pred = k;
      for (i = k+1; i < R; ++i) {
        if (empty[i]) {
          for (j = 0; j < C; j++) {
            s[i][j] = s[pred][j];
          }
        } else {
          pred = i;
        }
      } */

      cout << "Case #" << _case << ":\n";

      for (i = 0; i < R; i++) {
        cout << s[i] << "\n";
      }
  }
  return 0;
}
