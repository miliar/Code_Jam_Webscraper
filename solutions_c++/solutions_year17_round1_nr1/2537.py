#include <iostream>
using namespace std;

int T, R, C;
char ch;
char b[26][26];


int main(int argc, char** argv) {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> R >> C;
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        cin >> b[c][r];
      }
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        if (b[c][r] != '?') {
          for (int r1 = r + 1; r1 < R; ++r1) {
            if (b[c][r1] != '?') break;
            b[c][r1] = b[c][r];
          }
          for (int r1 = r - 1; r1 >= 0; --r1) {
            if (b[c][r1] != '?') break;
            b[c][r1] = b[c][r];
          }
        }
      }
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        if (b[c][r] != '?') {
          for (int c1 = c + 1; c1 < C; ++c1) {
            if (b[c1][r] != '?') break;
            b[c1][r] = b[c][r];
          }
          for (int c1 = c - 1; c1 >= 0; --c1) {
            if (b[c1][r] != '?') break;
            b[c1][r] = b[c][r];
          }
        }
      }
    }

    cout << "Case #" << (t + 1) << ":\n";
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        cout << b[c][r];
      }
      cout << endl;
    }

  }
}
