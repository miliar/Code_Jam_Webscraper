#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int r, c;
    cin >> r >> c;

    vector<vector<char>> v(r, vector<char>(c));

    for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j)
        cin >> v[i][j];

    int first_row = 0;

    for (int i = 0; i < r; ++i) {
      int j = 0;
      for (; j < c; ++j) {
        if (v[i][j] != '?')
          break;
      }
      if (j < c) {
        first_row = i;
        break;
      }
    }

    for (int i = first_row; i < r; ++i) {
      char letter = 0;
      for (int j = 0; j < c; ++j) {
        if (v[i][j] != '?') {
          letter = v[i][j];
          break;
        }
      }

      if (letter == 0) {
        for (int j = 0; j < c; ++j) {
          v[i][j] = v[i - 1][j];
        }
      } else {
        int j = 0;
        while (j < c) {
          while (j < c && (v[i][j] == '?' || v[i][j] == letter)) {
            v[i][j] = letter;
            ++j;
          }
          if (j < c) {
            letter = v[i][j];
          }
        }
      }
    }

    for (int i = first_row - 1; i >= 0; --i) {
      for (int j = 0; j < c; ++j) {
        v[i][j] = v[i + 1][j];
      }
    }

    cout << "Case #" << test << ":" << endl;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cout << v[i][j];
      }
      cout << endl;
    }
  }
}
