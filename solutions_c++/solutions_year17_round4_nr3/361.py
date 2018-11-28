#include<bits/stdc++.h>
using namespace std; 
typedef long long ll;
typedef double D;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define MP make_pair 
#define A first 
#define B second 
#define PB push_back 
#define FR(i, a, b) for(int i=(a); i<(b); i++) 
#define FOR(i, n) FR(i, 0, n) 
#define RF(i, a, b) for(int i=(b)-1; i>=(a); i--) 
#define ROF(i, n) RF(i, 0, n) 
#define EACH(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it) 

int R, C;
char grid[50][100];
int lasers[50][100];      // 1 vertical, 2 horizontal
bool found = false;

bool inbounds(int i, int j) {
  return i >= 0 && i < R && j >= 0 && j < C;
} 

bool has_empty_cells(const vvi& grid_copy) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (grid[i][j] == '.' && grid_copy[i][j] == 0) return true;
    }
  }
  return false;
}

ii next_coord(int i, int j) {
  if (j == C-1) {
    return MP(i+1, 0);
  } 
  return MP(i, j+1);
}

bool IsLaser(int i, int j) {
  return grid[i][j] == '|' || grid[i][j] == '-';
}

bool HasLShape() {
  for (int i = 0; i < C - 1; i++) {
    for (int j = 0; j < R - 1; j++) {
      if (IsLaser(i,j)) {
        if (IsLaser(i+1, j) && IsLaser(i, j+1)) return true;
      }
    }
  }
  return false;
}

bool IsImpossible(vvi grid_copy) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (grid[i][j] == '.' && grid_copy[i][j] == 0) {
        // Make sure has laser that can be set in the future to cover it.
        // has vertical laser?
        bool has_vert = false;
        for (int ni = i-1; ni >= 0; ni--) {
          if (!inbounds(ni, j)) break;
          if (grid[ni][j] == '#') break;
          if (IsLaser(ni, j)) {
            has_vert = true;
            break;
          }
        }
        for (int ni = i+1; ni < 10000; ni++) {
          if (!inbounds(ni, j)) break;
          if (grid[ni][j] == '#') break;
          if (IsLaser(ni, j)) {
            has_vert = true;
            break;
          }
        }
        
        // Has horizontal?
        bool has_hor = false;
        for (int nj = j-1; nj >= 0; nj--) {
          if (!inbounds(i, nj)) break;
          if (grid[i][nj] == '#') break;
          if (IsLaser(i, nj)) {
            has_hor = true;
            break;
          }
        }
        for (int nj = j+1; nj < 100000; nj++) {
          if (!inbounds(i, nj)) break;
          if (grid[i][nj] == '#') break;
          if (IsLaser(i, nj)) {
            has_hor = true;
            break;
          }
        }

        if (!has_vert && !has_hor) return true;
      }
    }
  }
  return false;
}

void dfs(int i, int j, vvi grid_copy) {
  //cout << "dfs visiting: " << i << " " << j << endl;
  // Need pruning conditions.
  if (IsImpossible(grid_copy)) return;
  
  if (i == R) {
    if (!has_empty_cells(grid_copy)) found = true;
    return;
  }
  if (grid[i][j] == '-' || grid[i][j] == '|') {
    //cout << "Found laser: " << i << " " << j << endl;
    // Try horizontal 
    lasers[i][j] = 2;
    vvi grid_copy_copy = grid_copy;
    bool good = true;
    grid_copy_copy[i][j] = '-';
    for (int nj = j+1; nj < 1000; nj++) {
      if (!inbounds(i, nj)) break;
      if (grid[i][nj] == '#') break;
      if (grid[i][nj] == '-' || grid[i][nj] == '|') {
        good = false;
        break;
      }
      grid_copy_copy[i][nj] = 1;
    }
    for (int nj = j-1; nj >= 0; nj--) {
      if (!inbounds(i, nj)) break;
      if (grid[i][nj] == '#') break;
      if (grid[i][nj] == '-' || grid[i][nj] == '|') {
        good = false;
        break;
      }
      grid_copy_copy[i][nj] = 1;
    }
    if (good) {
      //cout << "good horizontal: " << i << " " << j << endl;
      ii ncoord = next_coord(i, j);
      dfs(ncoord.first, ncoord.second, grid_copy_copy);
      if (found) return;
    }

    // Try vertical
    lasers[i][j] = 1;
    grid_copy_copy = grid_copy;
    good = true;
    grid_copy_copy[i][j] = '|';
    for (int ni = i+1; ni < 1000; ni++) {
      if (!inbounds(ni, j)) break;
      if (grid[ni][j] == '#') break;
      if (grid[ni][j] == '-' || grid[ni][j] == '|') {
        good = false;
        break;
      }
      grid_copy_copy[ni][j] = 1;
    }
    for (int ni = i-1; ni >= 0; ni--) {
      if (!inbounds(ni, j)) break;
      if (grid[ni][j] == '#') break;
      if (grid[ni][j] == '-' || grid[ni][j] == '|') {
        good = false;
        break;
      }
      grid_copy_copy[ni][j] = 1;
    }
    if (good) {
      //cout << "good vertical: " << i << " " << j << endl;
      ii ncoord = next_coord(i, j);
      dfs(ncoord.first, ncoord.second, grid_copy_copy);
    }
  }
  else { /// not laser
    ii ncoord = next_coord(i, j);
    dfs(ncoord.first, ncoord.second, grid_copy);
    if (found) return;
  }
}

void PrintGrid() {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cout << grid[i][j];
    }
    cout << endl;
  }
}

void PrintAns() {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (grid[i][j] == '|' || grid[i][j] == '-') {
        if (lasers[i][j] == 1) cout << '|';
        else cout << '-';
      } else {
        cout << grid[i][j];
      }
    }
    cout << endl;
  }
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
      string s;
      cin >> s;
      for (int j = 0; j < C; j++) grid[i][j] = s[j];
    }
    if (HasLShape()) {
      cout << "Case #" << tt << ": IMPOSSIBLE\n";
      continue;
    }


    found = false;
    for (int i = 0; i < 50; i++) {
      for (int j = 0; j < 100; j++) lasers[i][j] = 0;
    }
    vvi grid_copy(R, vi(C));
    //PrintGrid();
    dfs(0, 0, grid_copy);
    cout << "Case #" << tt << ": ";
    if (found) {
      cout << "POSSIBLE\n";
      PrintAns();
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
  return 0;
}

