#include <iostream>
#include <unordered_set>
#include <cstring>
#include <vector>

using namespace std;
typedef vector<char> vec_c_t;
typedef vector<vec_c_t> vec2d_c_t;

void expand_h(vec2d_c_t& c, int R, int C, int i, int j) {
  char p = c[i][j];
  for (int idx = j - 1; idx >= 0; --idx) {
    if (c[i][idx] != '?') break;
    c[i][idx] = p;
  }
  for (int idx = j + 1; idx < C; ++idx) {
    if (c[i][idx] != '?') break;
    c[i][idx] = p;
  }
}

void expand_v(vec2d_c_t& c, int R, int C, int i, int j) {
  char p = c[i][j];
  for (int idx = i - 1; idx >= 0; --idx) {
    if (c[idx][j] != '?') break;
    c[idx][j] = p;
  }
  for (int idx = i + 1; idx < R; ++idx) {
    if (c[idx][j] != '?') break;
    c[idx][j] = p;
  }
}

void work(vec2d_c_t& c, int R, int C) {
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (c[i][j] != '?') {
        expand_h(c, R, C, i, j);
      }
    }
  }
  for (int j = 0; j < C; ++j) {
    for (int i = 0; i < R; ++i) {
      if (c[i][j] != '?') {
        expand_v(c, R, C, i, j);
      }
    }
  }
  for (int i = 0; i < c.size(); ++i) {
    for (int j = 0; j < c[i].size(); ++j) {
      cout << c[i][j];
    }
    cout << endl;
  }
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int R, C;
    cin >> R >> C;
    vec2d_c_t c(R, vec_c_t(C));
    cout << "Case #" << i+1 << ":" << endl;
    for (int i = 0; i < R; ++i) {
      string s;
      cin >> s;
      for (int j = 0; j < C; ++j) {
        c[i][j] = s[j];
      }
    }
    work(c, R, C);
  }
  return 0;
}

