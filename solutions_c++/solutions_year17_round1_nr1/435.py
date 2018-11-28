#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int DIM_MAX = 30;
int R, C;
char cake[DIM_MAX][DIM_MAX];

void init() {
  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++)
      cin >> cake[i][j];
  }
}

void fill_row(int r) {
  char last = '?';
  for (int i = 0; i < C; i++) {
    if (cake[r][i] == '?') continue;

    last = cake[r][i];
    for (int j = i - 1; j >= 0; j--) {
      if (cake[r][j] != '?') break;
      cake[r][j] = last;
    }
  }

  for (int i = 0; i < C; i++) {
    if (last != '?' && cake[r][i] == '?')
      cake[r][i] = last;
  }
}

void solve_case(int t) {
  init();

  for (int i = 0; i < R; i++)
    fill_row(i);

  for (int i = 1; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (cake[i][j] == '?')
        cake[i][j] = cake[i-1][j];
    }
  }

  for (int i = R - 2; i >= 0; i--) {
    for (int j = 0; j < C; j++) {
      if (cake[i][j] == '?')
        cake[i][j] = cake[i+1][j];
    }
  }

  cout << "Case #" << t << ":\n";
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++)
      cout << cake[i][j];
    cout << "\n";
  }
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
