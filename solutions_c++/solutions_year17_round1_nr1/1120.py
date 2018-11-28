#include <iostream>
#include <algorithm>
using namespace std;

char** solve(int r, int c, char **A) {
  bool done[30];
  for (int i = 0; i < 30; ++i) {
    done[i] = false;
  }
  for (int j = 0; j < c; ++j) {
    for (int i = 0; i < r; ++i) {
      char val = A[i][j];
      if (val != '?' && (!done[val-'A'])) {
        // Up
        int k = i - 1;
        while (k >= 0 && A[k][j] == '?') {
          A[k][j] = val;
          k--;
        }
        int up = k+1;
        // Down
        k = i + 1;
        while (k < r && A[k][j] == '?') {
          A[k][j] = val;
          k++;
        }
        int down = k-1;
        //cout << val << "-" << up << "<>" << down << endl;
        // Left
        bool isempty = true;
        int l = j - 1;
        while (l >= 0 && isempty) {
          // Check column
          for (int k = up; k <= down; ++k) {
            if (A[k][l] != '?') {
              isempty = false;
              break;
            }
          }
          // Fill if empty
          if (isempty) {
            for (int k = up; k <= down; ++k) {
              A[k][l] = val;
            }
          }
          l--;
        }
        // Right
        isempty = true;
        l = j + 1;
        while (l < c && isempty) {
          // Check column
          for (int k = up; k <= down; ++k) {
            if (A[k][l] != '?') {
              isempty = false;
              break;
            }
          }
          // Fill if empty
          if (isempty) {
            for (int k = up; k <= down; ++k) {
              A[k][l] = val;
            }
          }
          l++;
        }
              done[val-'A'] = true;
      }

    }
  }
  return A;
}

void tcase(int t) {
  int r, c;
  cin >> r >> c;
  char **A = new char* [r];
  for (int i = 0; i < r; ++i) {
    A[i] = new char[c];
    string s;
    cin >> s;
    for (int j = 0; j < s.size(); ++j) {
      A[i][j] = s[j];
    }
  }
  char **B = solve(r, c, A);
  cout << "Case #" << t+1 << ": " << endl;
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      cout << B[i][j];
    }
    cout << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    tcase(i);
  }
  return 0;
}
