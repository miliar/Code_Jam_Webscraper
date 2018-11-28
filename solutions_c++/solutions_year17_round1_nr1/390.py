#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>
#include <utility>

using namespace std;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }

void solve() {
  int r = next< int >();
  int c = next< int >();
  vector< string > field;
  for (int i = 0; i < r; ++i) {
    field.push_back(next<string>());
  }
  for (int i = 0; i < r; ++i) {
    for (int j = 1; j < c; ++j) {
      field[i][j] = field[i][j] == '?' ? field[i][j - 1] : field[i][j];
    }
    for (int j = c - 2; j >= 0; --j) {
      field[i][j] = field[i][j] == '?' ? field[i][j + 1] : field[i][j];
    }
  }
  for (int i = 0; i < c; ++i) {
    for (int j = 1; j < r; ++j) {
      field[j][i] = field[j][i] == '?' ? field[j - 1][i] : field[j][i];
    }
    for (int j = r - 2; j >= 0; --j) {
      field[j][i] = field[j][i] == '?' ? field[j + 1][i] : field[j][i];
    }
  }
  cout << endl;
  for (int i = 0; i < r; ++i) {
    cout << field[i] << endl;
  }
}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
