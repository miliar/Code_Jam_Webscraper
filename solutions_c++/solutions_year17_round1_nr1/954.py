#include <assert.h>
#include <iostream>
#include <string>

using namespace std;

int R, C;
string s[32];
bool viz[32][32];

void fill(int r, int c) {
  int c0 = c - 1;
  while (c0 >= 0) {
    if (s[r][c0] != '?') {
      break;
    }
    --c0;
  }

  int c1 = c + 1;
  while (c1 < C) {
    if (s[r][c1] != '?') {
      break;
    }
    ++c1;
  }

  int r0 = r - 1;
  while (r0 >= 0) {
    bool pos = true;
    for (int cc = c0 + 1; cc < c1; ++cc) {
      if (s[r0][cc] != '?') {
        pos = false;
        break;
      }
    }
    if (!pos) {
      break;
    }
    --r0;
  }

  int r1 = r + 1;
  while (r1 < R) {
    bool pos = true;
    for (int cc = c0 + 1; cc < c1; ++cc) {
      if (s[r1][cc] != '?') {
        pos = false;
        break;
      }
    }
    if (!pos) {
      break;
    }
    ++r1;
  }

  for (int rr = r0 + 1; rr < r1; ++rr) {
    for (int cc = c0 + 1; cc < c1; ++cc) {
      assert(s[rr][cc] == '?' || s[rr][cc] == s[r][c]);
      s[rr][cc] = s[r][c];
      viz[rr][cc] = true;
    }
  }
}

int main() {
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
      cin >> s[i];
      for (int j = 0; j < C; ++j) {
        viz[i][j] = false;
      }
    }
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (!viz[i][j] && s[i][j] != '?') {
          fill(i, j);
        }
      }
    }

    printf("Case #%d:\n", t + 1);
    for (int i = 0; i < R; ++i) {
      cout << s[i] << endl;
    }
  }
}
