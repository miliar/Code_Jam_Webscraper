#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#define rep(i, n) for (int i = 0; i < n; ++i)

using namespace std;

long join (int left, int right) {
  long l = (long) left;
  return l << 32 & ((long) right);
}

int l(unsigned long n) {
  return (int) (n >> 32);
}
int ri(unsigned long n) {
  return (int) (n);
}

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  rep(i, t) {
    string solution;
    int r, c;
    cin >> r >> c;
    vector<string> lines;
    rep(j, r) {
      string in;
      cin >> in;
      lines.push_back(in);
    }
    rep(j, r) {
      char ch = '?';
      rep(k, c) {
        if (lines[j][k] != '?')
          ch = lines[j][k];
        else
          lines[j][k] = ch;
      }
    }
    rep(j, r) {
      char ch = '?';
      for (int k = c - 1; k >= 0; --k) {
        if (lines[j][k] != '?')
          ch = lines[j][k];
        else
          lines[j][k] = ch;
      }
    }
    rep(j, c) {
      char ch = '?';
      rep(k, r) {
        if (lines[k][j] != '?')
          ch = lines[k][j];
        else
          lines[k][j] = ch;
      }
    }
    rep(j, c) {
      char ch = '?';
      for (int k = r - 1; k >= 0; --k) {
        if (lines[k][j] != '?')
          ch = lines[k][j];
        else
          lines[k][j] = ch;
      }
    }
    printf("Case #%d:\n", i + 1);
    for (string line : lines) {
      cout << line << endl;
    }
  }
}
