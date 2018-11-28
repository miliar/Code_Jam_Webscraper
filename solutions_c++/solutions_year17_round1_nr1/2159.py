#include <bits/stdc++.h>

using namespace std;

char grid[25][25];
char oldgrid[25][25];
int rows;
int cols;
set<char> seen;
map<char, vector<int>> bounds;
int remaining;

bool intersects(vector<int> a, vector<int> b) {
  return a[0] <= b[2] && a[2] >= b[0] && a[1] <= b[3] && a[3] >= b[1];
}

bool checkRange(vector<int> a, char ch) {
  for(char c : seen) {
    if(c != ch) {
      if(intersects(bounds[c], a))
        return false;
    }
  }
  return true;
}

bool recurse(int r, int c) {
  //cerr << "+" << r << " " << c << " " << remaining << " " << endl;
  if(r > rows || c > cols || remaining == 0)
    return true;

  if(checkRange({r, c, r, c}, 0)) {
    for(char ch: seen) {
      int ra = min(r, bounds[ch][0]);
      int ca = min(c, bounds[ch][1]);
      int rb = max(r, bounds[ch][2]);
      int cb = max(c, bounds[ch][3]);
      //cerr << ra << " " << ca << " " << rb << " " << cb << " " << ch << endl;
      if(checkRange({ra, ca, rb, cb}, ch)) {
        vector<int> old = bounds[ch];
        bounds[ch] = {ra, ca, rb, cb};
        int inc = (rb - ra) * (cb - ca) - (old[3] - old[1]) * (old[2] - old[0]); 
        remaining -= inc;
        if(r == 1) {
          if (recurse(r, c+1) && recurse(r+1, c))
            return true;
        }
        else
          if (recurse(r+1, c))
            return true;
        else {
          remaining += inc;
          bounds[ch] = old;
        }
      }
    }
    return false;
  }
  else {
    if(r == 1) {
      return recurse(r, c+1) && recurse(r+1, c);
    }
    else
      return recurse(r+1, c);
  }

}

int main() {
  int loops;
  cin >> loops;
  for(int loop = 1; loop <= loops; ++loop) {
    cin >> rows >> cols;

    seen.clear();
    bounds.clear();
    for(int r = 0; r < rows; ++r) {
      cin.ignore();
      for(int c = 0; c < cols; ++c) {
        cin >> grid[r][c];
        if(grid[r][c] != '?') seen.insert(grid[r][c]);
      }
    }

    for(char ch : seen) {
      int ra = 25, ca=25, rb = -1, cb=-1;
      for(int r = 0; r < rows; ++r) {
        for(int c = 0; c < cols; ++c) {
          if(grid[r][c] == ch) {
            ra = min(ra, r);
            rb = max(rb, r);
            ca = min(ca, c);
            cb = max(cb, c);
          }
        }
      }
      //fill(ra, ca, rb, cb, ch);
      bounds[ch] = {ra+1, ca+1, rb+1, cb+1};
    }

    remaining = 0;
    for(int r = 0; r < rows; ++r) {
      for(int c = 0; c < cols; ++c) {
        if(grid[r][c] == '?')
          remaining++;
      }
    }

    recurse(1, 1);
    for(char ch : seen) {
      for(int r = bounds[ch][0]; r <= bounds[ch][2]; r++) {
        for(int c = bounds[ch][1]; c <= bounds[ch][3]; c++) {
          grid[r-1][c-1] = ch;
        }
      }
    }

    cout << "Case #" << loop << ":" << endl;
    for(int r = 0; r < rows; ++r) {
      for(int c = 0; c < cols; ++c) {
        cout << grid[r][c];
      }
      cout << endl;
    }




  }
}
