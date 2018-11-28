#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>

#if DEBUG
#include "prettyprint.hpp"
#define print_container(c) cout << c << endl;
#endif

using namespace std;

string FILENAME = "a-large";

vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d:\n", case_id);

    int r, c;
    scanf("%d %d", &r, &c);

    vector<string> grid;
    for (int i = 0; i < r; i++) {
      char c[256];
      scanf("%s", c);
      string s(c);
      grid.push_back(s);
    }

    set<char> seen;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] != '?' && seen.find(grid[i][j]) == seen.end()) {
          seen.insert(grid[i][j]);
          int min_c = j;
          int max_c = j;
          // right
          for (int k = 1; k < c; k++) {
            if (j + k < c && grid[i][j + k] == '?') {
              grid[i][j + k] = grid[i][j];
              max_c++;
            } else {
              break;
            }
          }
          // left
          for (int k = 1; k < c; k++) {
            if (j - k >= 0 && grid[i][j - k] == '?') {
              grid[i][j - k] = grid[i][j];
              min_c--;
            } else {
              break;
            }
          }
          // up
          for (int k = 1; k < r; k++) {
            if (i + k >= r) {
              break;
            }
            bool good_row = true;
            for (int l = min_c; l <= max_c; l++) {
              if (grid[i + k][l] != '?') {
                good_row = false;
              }
            }
            if (!good_row) {
              break;
            }
            for (int l = min_c; l <= max_c; l++) {
              grid[i + k][l] = grid[i][j];
            }
          }
          // down
          for (int k = 1; k < r; k++) {
            if (i - k < 0) {
              break;
            }
            bool good_row = true;
            for (int l = min_c; l <= max_c; l++) {
              if (grid[i - k][l] != '?') {
                good_row = false;
              }
            }
            if (!good_row) {
              break;
            }
            for (int l = min_c; l <= max_c; l++) {
              grid[i - k][l] = grid[i][j];
            }
          }
        }
      }
    }
    for (int i = 0; i < r; i++) {
      printf("%s\n", grid[i].c_str());
    }
  }
  fflush(stdout);
}
