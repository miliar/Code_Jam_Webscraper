#include <iostream>
#include <fstream>

#include <stack>
#include <queue>
#include <deque>
#include <vector>

#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

#include <cmath>

#include <cassert>

#include <algorithm>

using namespace std;

ifstream fin("///Users/Zetilov/Downloads/A-large.in-2.txt");
ofstream fout("output.txt");

void solve(long long cs)
{
  int n, m;
  fin >> n >> m;
  vector<vector<char>> v(n, vector<char>(m));
  for (auto& x : v) {
    for (auto& y : x) {
      fin >> y;
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (v[i][j] == '?') {
        continue;
      }
      int k = j + 1;
      while (k < m && v[i][k] == '?') {
        v[i][k++] = v[i][j];
      }
    }
    int j = 0;
    while (j < m && v[i][j] == '?') {
      ++j;
    }
    if (j < m) {
      for (int k = 0; k < j; ++k) {
        v[i][k] = v[i][j];
      }
    }
  }
  for (int i = 1; i < n; ++i) {
    if (v[i] == vector<char>(m, '?')) {
      v[i] = v[i - 1];
    }
  }
  int i;
  for (i = 0; i < n; ++i) {
    if (v[i] != vector<char>(m, '?')) {
      break;
    }
  }
  for (int k = 0; k < i; ++k) {
    v[k] = v[i];
  }
  for (auto x : v) {
    for (auto y : x) {
      fout << y;
    }
    fout << "\n";
  }
}


int main()
{
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  cout.setf(ios_base::fixed);
  cout.precision(28);

  long long T;
  fin >> T;
  for (long long cs = 1; cs <= T; ++cs) {
    cout << cs << endl;

    fout << "Case #" << cs << ": ";
    fout << endl;
    solve(cs);
  }
  return 0;
}