#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <cstdint>

using namespace std;

vector<string> lines;

int main() {
  int T = 0;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    int R = 0, C = 0;
    scanf("%d %d\n", &R, &C);
    lines.clear();
    for (int i = 0; i < R; ++i) {
      string line;
      getline(cin, line);
      lines.push_back(line);
    }
    for (int i = 0; i < R; ++i) {
      char c = 0;
      char firstC = 0;
      for (int j = 0; j < C; ++j) {
        if (lines[i][j] != '?') {
          c = lines[i][j];
          if (firstC == 0) {
            firstC = c;
          }
        } else if (lines[i][j] == '?' && c != 0) {
          lines[i][j] = c;
        }
      }
      if (firstC != 0) {
        for (int j = 0; j < C; ++j) {
          if (lines[i][j] == '?') {
            lines[i][j] = firstC;
          }
        }
      }
    }
    for (int i = 0; i < R; ++i) {
      bool f = false;
      for (int j = 0; j < C; ++j) {
        if (lines[i][j] != '?') {
          f = true;
          break;
        }
      }
      if (f) {
        for (int k = 0; k < i; ++k) {
          if (lines[k][0] == '?') {
            lines[k] = lines[i];
          }
        }
      }
    }
    for (int i = R - 1; i >= 0; --i) {
      bool f = false;
      for (int j = 0; j < C; ++j) {
        if (lines[i][j] != '?') {
          f = true;
          break;
        }
      }
      if (f) {
        for (int k = i + 1; k < R; ++k) {
          if (lines[k][0] == '?') {
            lines[k] = lines[i];
          }
        }
        break;
      }
    }
    cout << "Case #" << t << ":" << endl;
    for (int i = 0; i < R; ++i) {
      cout << lines[i] << endl;
    }
  }
}
