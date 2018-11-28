#include <iostream>
#include <fstream>
using namespace std;

int T, R, C, row;
char grid[30][30], colour;

int main() {
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> R >> C;
    for (int i = 0 ; i < R ; i++) {
      for (int j = 0 ; j < C ; j++) {
        fin >> grid[i][j];
      }
    }
    for (int i = 0 ; i < R ; i++) {
      int start = 0;
      while (start < C && grid[i][start] == '?') {
        start++;
      }
      if (start < C) {
        colour = grid[i][start];
        for (int j = 0 ; j < C ; j++) {
          if (grid[i][j] == '?') {
            grid[i][j] = colour;
          } else {
            colour = grid[i][j];
          }
        }
      }
    }
    for (int i = 0 ; i < R ; i++) {
      if (grid[i][0] == '?') {
        row = i;
        while (row < R && grid[row][0] == '?') {
          row++;
        }
        if (row == R) {
          row = i;
          while (row >= 0 && grid[row][0] == '?') {
            row--;
          }
        }
        for (int j = 0 ; j < C ; j++) {
          grid[i][j] = grid[row][j];
        }
      }
    }
    fout << "Case #" << t << ":" << endl;
    for (int i = 0 ; i < R ; i++) {
      for (int j = 0 ; j < C ; j++) {
        fout << grid[i][j];
      }
      fout << endl;
    }
  }
  return 0;
}

// ???????
// ??C??E?
// ???D???
// ???????