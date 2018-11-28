#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

using namespace std;

char grid[30][30];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

struct Foo {
  int min_i;
  int max_i;
  int min_j;
  int max_j;  
};

int main() {
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    int R,C;
    cin >> R >> C;
    
    for(int i = 0; i < R; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < C; j++) {
          grid[i][j] = s[j];
        }
    }
    
    // find if any rectangles we are "required" to make
    map<char, Foo> mm;
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
          char curr = grid[i][j];
          if (curr == '?')
            continue;
          int min_i = i;
          int max_i = i;
          int min_j = j;
          int max_j = j;
          
          for (int ii = 0; ii < R; ii++) {
            for (int jj = 0; jj < C; jj++) {
              if(ii == i && jj == j) {
                continue;
              }
              if (grid[ii][jj] == curr) {
                min_i = min(i, ii);
                max_i = max(i, ii);
                min_j = min(j, jj);
                max_j = max(j, jj);
              }
            }
          }
          
          Foo f;
          f.min_i = min_i;
          f.max_i = max_i;
          f.min_j = min_j;
          f.max_j = max_j;
          mm[curr] = f;
          //cout << "map: " << curr<< " " << min_i << " " << max_i << " " << min_j << " " << max_j << endl;
          
          // fill it
          for (int ii = min_i; ii <= max_i; ii++) {
            for (int jj = min_j; jj <= max_j; jj++) {
              grid[ii][jj] = curr;
            }
          } 
        }
    }
    // now try filling all squares
    for(int i = 0; i < R; i++) {
      for(int j = 0; j < C; j++) {
        if (grid[i][j] == '?') {
          //cout << "trying to fill: "<< i << " " << j << endl;
          bool filled = false;
          for(int d = 0; d < 4 && !filled; d++) {
            int ddi = dx[d];
            int ddj = dy[d];
            int ci = i;
            int cj = j;
            int width;
            while (ci >= 0 && cj >= 0 && ci < R && cj < C && !filled) {
              if (grid[ci][cj] != '?') {
                char curr = grid[ci][cj];
                //cout << "trying to fill with: " << ci << " " << cj << " " << curr << endl;
                // check if can fill
                // CASE 1
                if (ddi == 0) {
                  int max_i = mm[curr].max_i;
                  int min_i = mm[curr].min_i;
                  bool good = true;
                  //cout << "A" << endl;
                  for (int k = cj; k != j-ddj && good; k-=ddj) {
                    for (int z = min_i; z <= max_i; z++) {
                      if (grid[z][k] != '?' && grid[z][k] != curr) {
                        //cout << "good set to false at: " << z << " " << k << " " << grid[z][k] << endl;
                        good = false;
                        break;
                      }
                    }
                  }
                  //cout << "B" << endl;
                  
                  if (good) {
                    filled = true;
                    //cout << "good is true: " << cj << " " << j << " " << min_i << " " << max_i <<endl;
                    for (int k = cj; k != j-ddj; k-=ddj) {
                      for (int z = min_i; z <= max_i; z++) {
                        grid[z][k] = curr;
                      }
                    }
                    mm[curr].max_j = max(j, mm[curr].max_j);
                    mm[curr].min_j = min(j, mm[curr].min_j);
                    break;
                  }
                  
                }
                // CASE 2
                else if (ddj == 0) {
                  int max_j = mm[curr].max_j;
                  int min_j = mm[curr].min_j;
                  bool good = true;
                  for (int k = ci; k != i-ddi && good; k-=ddi) {
                    for (int z = min_j; z <= max_j; z++) {
                      if (grid[k][z] != '?' && grid[k][z] != curr) {
                        good = false;
                        //cout << "good set to false at: " << k << " " << z << " " << grid[k][z] << endl;
                        break;
                      }
                    }
                  }
                  if (good) {
                    filled = true;
                    //cout << "good is true: " << ci << " " << i << " " << min_j << " " << max_j <<endl;
                    for (int k = ci; k != i-ddi; k-=ddi) {
                      for (int z = min_j; z <= max_j; z++) {
                        grid[k][z] = curr;
                      }
                    }
                    mm[curr].max_i = max(i, mm[curr].max_i);
                    mm[curr].min_i = min(i, mm[curr].min_i);
                    break;
                  }
                  
                }
                else {
                  //cout << "wtf" << endl;
                }
              }
              ci += ddi;
              cj += ddj;
            }
          
          }
        }
      }
    }

    cout << "Case #" << tt << ":" << endl;
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
          cout << grid[i][j];
        }
        cout << endl;
    }

  }

  return 0;
}


