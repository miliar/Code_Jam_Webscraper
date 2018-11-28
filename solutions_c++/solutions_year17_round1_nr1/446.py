#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int T,R,C;

ifstream fin("A.in");
ofstream fout("A.out");

char grid[30][30];
bool hasLetter[30];

void fillrow(int n) {
  int firstcol = 0;
  for (firstcol = 0; grid[n][firstcol] == '?'; firstcol++);
  for (int i = 0; i < firstcol; i++) {
    grid[n][i] = grid[n][firstcol];
  }
  for (int i = firstcol; i < C; i++) {
    if (grid[n][i] == '?') {
      grid[n][i] = grid[n][i-1];
    }
  }
}

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    int firstind = 99;
    fin >> R >> C;
    for (int i = 0; i < R; i++) {
      string input;
      fin >> input;
      bool flag = false;
      for (int j = 0; j < C; j++) {
        grid[i][j] = input[j];
        if (input[j] != '?') flag = true;
      }
      hasLetter[i] = flag;
      if (flag) firstind = min(firstind,i);
    }
    fillrow(firstind);
    for (int i = 0; i < firstind; i++) {
      for (int j = 0; j < C; j++) grid[i][j] = grid[firstind][j];
    }
    for (int i = firstind+1; i < R; i++) {
      if (hasLetter[i]) fillrow(i);
      else {
        for (int j = 0; j < C; j++) grid[i][j] = grid[i-1][j];
      }
    }
    fout << "Case #" << tt << ":\n";
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        fout << grid[i][j];
      }
      fout << "\n";
    }
  }
  return 0;
}