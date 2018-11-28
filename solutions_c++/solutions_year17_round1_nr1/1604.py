#include <bits/stdc++.h>

using namespace std;

vector<string> foo(vector<string> &in) {
  vector<string> ret;
  for (int i = 0; i < in.size(); i++) {
    string build = in[i];
    // forwards
    int copy = build[0];
    for (int j = 0; j < build.size(); j++) {
      if (build[j] == '?') {
        build[j] = copy;
      } else {
        copy = build[j];
      }
    }

    // backwards
    copy = build[build.size() - 1];
    for (int j = build.size() - 1; j >= 0; j--) {
      if (build[j] == '?') {
        build[j] = copy;
      } else {
        copy = build[j];
      }
    }
    ret.push_back(build);
  }

  bool fixed = false;
  while (!fixed) {
    fixed = true;
    for (int i = 0; i < in.size(); i++) {
      if (ret[i][0] == '?') {
        fixed = false;
        if (i == 0) {
          if (ret[i + 1][0] != '?') {
            for (int j = 0; j < ret[i + 1].size(); j++) {
              ret[i][j] = ret[i + 1][j];
            }
          }
        } else if (i == in.size()) {
          if (ret[i - 1][0] != '?') {
            for (int j = 0; j < ret[i - 1].size(); j++) {
              ret[i][j] = ret[i - 1][j];
            }
          }
        } else {
          if (ret[i - 1][0] != '?') {
            for (int j = 0; j < ret[i - 1].size(); j++) {
              ret[i][j] = ret[i - 1][j];
            }
          } else if (ret[i + 1][0] != '?') {
            for (int j = 0; j < ret[i + 1].size(); j++) {
              ret[i][j] = ret[i + 1][j];
            }
          }
        }
      }
    }
  }
  return ret;
}

int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    int rows;
    int cols;
    cin >> rows;
    cin >> cols;
    vector<string> grid;
    for (int j = 0; j < rows; j++) {
      string in;
      cin >> in;
      grid.push_back(in);
    }
    vector<string> result = foo(grid);
    cout << "Case #" << i + 1 << ": " << endl;
    for (int j = 0; j < rows; j++) {
      cout << result[j] << endl;
    }
  }
}
