#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

int r, c;
vector<string> grid;

char find_val(int row, int col, int rd, int cd) {
  if (row >= r || col >= c || row < 0 || col < 0) {
    return '?';
  }
  if (grid[row][col] != '?') {
    return grid[row][col];
  }
  return find_val(row + rd, col + cd, rd, cd);
}

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> r >> c;
    grid.clear();
    grid.resize(r);
    for (int i = 0; i < r; i++) {
      cin >> grid[i];
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
	if (grid[i][j] == '?') {
	  char c = find_val(i, j, 0, 1);
	  if (c == '?') {
	    c = find_val(i, j, 0, -1);
	  }
	  grid[i][j] = c;
	}
      }
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
	if (grid[i][j] == '?') {
	  char c = find_val(i, j, 1, 0);
	  if (c == '?') {
	    c = find_val(i, j, -1, 0);
	  }
	  grid[i][j] = c;
	}
      }
    }
    cout << "Case #" << t << ":" << endl;
    for (int i = 0; i < r; i++) {
      cout << grid[i] << endl;
    }
  }
  return 0;
}
