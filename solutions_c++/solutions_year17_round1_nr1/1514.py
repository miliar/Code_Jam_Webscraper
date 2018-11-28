#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":" << endl;
    int r, c;
    cin >> r >> c;
    vector<string> s(r);
    for (int i = 0; i < r; i++)
      cin >> s[i];
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (s[i][j] != '?') {
          for (int k = j - 1; k >= 0 && s[i][k] == '?'; k--)
            s[i][k] = s[i][j];
        }
      }
      for (int j = c - 1; j >= 0; j--) {
        if (s[i][j] != '?') {
          for (int k = j + 1; k < c && s[i][k] == '?'; k++)
            s[i][k] = s[i][j];
        }
      }
      if (i) {
        for (int j = 0; j < c; j++) {
          if (s[i][j] == '?')
            s[i][j] = s[i - 1][j];
        }
      }
    }
    for (int i = r - 2; i >= 0; i--) {
      for (int j = 0; j < c; j++) {
        if (s[i][j] == '?')
          s[i][j] = s[i + 1][j];
      }
    }
    for (int i = 0; i < r; i++)
      cout << s[i] << endl;
  }
  return 0;
}