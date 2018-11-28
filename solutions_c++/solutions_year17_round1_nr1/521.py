#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ofstream fout;
    ifstream fin;
    fin.open("input.txt");
    fout.open("output.txt");
    int t; fin >> t;
    for(int tc = 1; tc <= t; tc++) {
        int r, c; fin >> r >> c;
        char grid[r][c];
        for(int i = 0; i < r; i++) {
          for(int j = 0; j < c; j++) {
            fin >> grid[i][j];
          }
        }

        for(int i = 0; i < r; i++) {
          for(int j = 1; j < c; j++) {
            if(grid[i][j] == '?') {
              grid[i][j] = grid[i][j - 1];
            }
          }
          for(int j = c - 2; j >= 0; j--) {
            if(grid[i][j] == '?') {
              grid[i][j] = grid[i][j + 1];
            }
          }
        }

        for(int i = 1; i < r; i++) {
          for(int j = 0; j < c; j++) {
            if(grid[i][j] == '?') {
                grid[i][j] = grid[i - 1][j];
            }
          }
        }

        for(int i = r - 2; i >= 0; i--) {
          for(int j = 0; j < c; j++) {
            if(grid[i][j] == '?') {
                grid[i][j] = grid[i + 1][j];
            }
          }
        }

        fout << "Case #" << tc << ":" << endl;
        for(int i = 0; i < r; i++) {
          for(int j = 0; j < c; j++) {
            fout << grid[i][j];
          }
          fout << endl;
        }
    }
    return 0;
}
