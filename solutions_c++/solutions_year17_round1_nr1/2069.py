#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

char cake[25][25];

void solve(int R, int C) {
  for (int r = 0; r < R; ++r) {
    char letter = '?';

    for (int c = 0; c < C; ++c) {
      if (cake[r][c] != '?') {
        letter = cake[r][c] ;
        break;
      } 
    }

    if (letter == '?') continue;
    for (int c = 0; c < C; ++c) {
      if (cake[r][c] == '?') cake[r][c] = letter;
      else letter = cake[r][c];
    }
  }

  for (int c = 0; c < C; ++c) {
    char letter = '?';

    for (int r = 0; r < R; ++r) {
      if (cake[r][c] != '?') {
        letter = cake[r][c] ;
        break;
      } 
    }

    if (letter == '?') continue;
    for (int r = 0; r < R; ++r) {
      if (cake[r][c] == '?') cake[r][c] = letter;
      else letter = cake[r][c];
    }
  }

  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      cout << cake[r][c];
    }
    cout << '\n';
  }
}

int main() {
  int T;
  cin >> T;
  
  for (int t = 0; t < T; ++t) {
    int R, C;
    cin >> R >> C;
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        cin >> cake[r][c];
      }
    }

    cout << "Case #" << t + 1 << ": \n";
    solve(R, C);
  }

  return 0;
}