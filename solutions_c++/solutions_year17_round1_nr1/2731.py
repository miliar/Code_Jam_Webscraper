#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <iomanip>
#include <stack>
#include <sstream>
#include <queue>
#include <set>
#include <functional>
#include <ctime>

#define endl '\n'
#define eps 1e-9
#define ll long long int

using namespace std;

const int N = 50;
char grid[N][N];
bool seen[N], seen2[N][N];

int to_num(char a) {
  return (int)(a-'A');
}

int main() {
  #ifndef TEST
  	ios_base::sync_with_stdio(false);
  	cin.tie(0);
  #endif
  int T;
  cin >> T;
  for (int Case = 1; Case <= T; Case++) {
    int r, c;
    cin >> r >> c;
    for (int i = 0; i < N; i++) {
      seen[i] = false;
      for (int j = 0; j < N; j++) {
        seen2[i][j] = false;
      }
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cin >> grid[i][j];
      }
    }
    int i = 0, j = 0, dx = 1, dy = 0;
    for (int cnt = 0; cnt < r*c; cnt++) {
      seen2[i][j] = true;
      char cur = grid[i][j];
      if (cur != '?' && !seen[to_num(cur)]) {
        seen[to_num(cur)] = true;
        int r_low = i, r_high = i, c_low = j, c_high = j;
        for (; r_low > 0 && grid[r_low-1][j] == '?'; r_low--);
        for (; r_high < r-1 && grid[r_high+1][j] == '?'; r_high++);
        while (true) {
          bool works = true;
          if (c_low == 0) break;
          for (int k = r_low; k <= r_high; k++) {
            if (grid[k][c_low-1] != '?') {
              works = false;
              break;
            }
          }
          if (works) c_low--;
          else {
            break;
          }
        }
        while (true) {
          bool works = true;
          if (c_high == c-1) break;
          for (int k = r_low; k <= r_high; k++) {
            if (grid[k][c_high+1] != '?') {
              works = false;
              break;
            }
          }
          if (works) c_high++;
          else {
            break;
          }
        }
        for (int k = r_low; k <= r_high; k++) {
          for (int kk = c_low; kk <= c_high; kk++) {
            grid[k][kk] = cur;
          }
        }
      }
      int nxt_i = i+dx, nxt_j = j+dy;
      if (nxt_i >= 0 && nxt_i < r && nxt_j >= 0 && nxt_j < c && !seen2[nxt_i][nxt_j]) {
        i = nxt_i;
        j = nxt_j;
      }
      else {
        if (dx == 1) {
          dx = 0;
          dy = 1;
        }
        else if (dx == -1) {
          dx = 0;
          dy = -1;
        }
        else if (dy == 1) {
          dx = -1;
          dy = 0;
        }
        else if (dy == -1) {
          dx = 1;
          dy = 0;
        }
        i = i+dx;
        j = j+dy;
      }
    }
    cout << "Case #" << Case << ":\n";
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cout << grid[i][j];
        if (grid[i][j] == '?') {
          cerr << "FOUND QUESTIONMARK\n";
        }
      }
      cout << '\n';
    }
  }
}
