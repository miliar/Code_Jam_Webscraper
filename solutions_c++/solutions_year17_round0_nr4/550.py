#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <set>
#include <map>
#include <array>
#include <climits>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

typedef unsigned long long u64;

int main() {
  int t;
  cin >> t;

  for (int i_test = 0; i_test < t; ++i_test) {

    int n, m;
    cin >> n >> m;

    vector<bool> diag_p(2 * n - 1);
    vector<bool> diag_m(2 * n - 1);
    vector<bool> row(n);
    vector<bool> column(n);
    vector<int> plus(2 * n - 1, -1); // index - diag, value = col with +
    vector<int> x(n, -1); // index - row, value = col with x
    vector<vector<char>> changes(n);
    for (int i = 0; i < n; ++i) changes[i].resize(n);

    int points = 0;
    int change_count = 0;
    // vector<int> o(n); // index - row, value = col with o
    for (int i = 0; i < m; ++i) {
      char model;
      int r, c;
      cin >> model >> r >> c;
      --r;
      --c;

      if (model == 'x' || model == 'o') {
        x[r] = c;
        row[r] = true;
        column[c] = true;
        ++points;
      }

      if (model == '+' || model == 'o') {
        plus[r + c] = c;
        diag_p[r + c] = true;
        diag_m[n - 1 + r - c] = true;
        ++points;
      }
    }

    // first row -> +
    for (int c = 0; c < n; ++c) {
      if (!diag_p[0 + c] && !diag_m[n - 1 + 0 - c]) { // free diag - change to o
        diag_p[0 + c] = true;
        diag_m[n - 1 + 0 - c] = true;
        plus[0 + c] = c;
        if (changes[0][c] == 0) ++change_count;
        ++points;
        if (x[0] == c) {
          changes[0][c] = 'o';
        } else {
          changes[0][c] = '+';
        }
      }
    }

    // last row -> +
    for (int c = 0; c < n; ++c) {
      if (!diag_p[n - 1 + c] && !diag_m[n - 1 + (n - 1) - c]) { // free diag - change to o
        diag_p[n - 1 + c] = true;
        diag_m[n - 1 + (n - 1) - c] = true;
        if (changes[n - 1][c] == 0) ++change_count;
        ++points;
        if (x[n - 1] == c) {
          changes[n - 1][c] = 'o';
        } else {
          changes[n - 1][c] = '+';
        }
      }
    }

    // diag -> x
    for (int r = 0; r < n; ++r) {
      if (!row[r]) {
        for (int c = 0; c < n; ++c) {
          if (!column[c]) {
            row[r] = true;
            column[c] = true;
            x[r] = c;
            ++points;
            if (changes[r][c] == 0) ++change_count;
            if (plus[r + c] == c) {
              changes[r][c] = 'o';
            } else {
              changes[r][c] = 'x';
            }
            break;
          }
        }
      }
    }

    cout << "Case #" << i_test + 1 << ": " << points << " " << change_count << endl;
    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        if (changes[r][c] != 0) {
          cout << changes[r][c] << " " << r + 1 << " " << c + 1 << endl;
        }
      }
    }
    //cout << changes.str();
  }

  return 0;
}
