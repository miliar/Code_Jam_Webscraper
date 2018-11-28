#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int R, C;
vector<string> map;
vector<int> cs;
void greedy() {
  vector<pair<int,char>> cc;
  for(int c = 'A'; c <= 'Z'; c++) {
    int minRow = 99999999,maxRow = -1, minCol = 9999999,maxCol = -1;
    for(int row = 0; row < map.size(); row++) {
      for(int col = 0; col < map[row].size(); col++) {
        if(map[row][col] == c) {
          minRow = min(minRow,row);
          maxRow = max(maxRow,row);
          minCol = min(minCol,col);
          maxCol = max(maxCol,col);
        }
      }
    }
    if(maxRow != -1) {
      for(int row = minRow; row <= maxRow; row++) {
        for(int col = minCol; col <= maxCol; col++) {
          map[row][col] = c;
          cc.emplace_back(row * R + col, c);
        }
      }
    }
  }
  sort(cc.begin(), cc.end());
  cs.clear();
  for(int i = 0; i < cc.size(); i++) {
    cs.push_back(cc[i].second);
  }
  cc.clear();
}
void greedy2(bool mode = false) {
  for(int c: cs) {
    int minRow = 99999999,maxRow = -1, minCol = 9999999,maxCol = -1;
    for(int row = 0; row < map.size(); row++) {
      for(int col = 0; col < map[row].size(); col++) {
        if(map[row][col] == c) {
          minRow = min(minRow,row);
          maxRow = max(maxRow,row);
          minCol = min(minCol,col);
          maxCol = max(maxCol,col);
        }
      }
    }
    if(maxRow != -1) {
      // 行拡張
      bool ok = true;
      if(mode) {
        while(minRow > 0) {
          ok = true;
          for(int col = minCol; col <= maxCol; col++) {
            if(map[minRow - 1][col] != '?') ok = false;
          }
          if(ok) {
            minRow--;
          }else{
            break;
          }
        }
        while(maxRow + 1 < R) {
          ok = true;
          for(int col = minCol; col <= maxCol; col++) {
            if(map[maxRow + 1][col] != '?') ok = false;
          }
          if(ok) {
            maxRow++;
          }else{
            break;
          }
        }
      } else {
        while(minCol > 0) {
          ok = true;
          for(int row = minRow; row <= maxRow; row++) {
            if(map[row][minCol - 1] != '?') ok = false;
          }
          if(ok) {
            minCol--;
          }else{
            break;
          }
        }
        while(maxCol + 1 < C) {
          ok = true;
          for(int row = minRow; row <= maxRow; row++) {
            if(map[row][maxCol + 1] != '?') ok = false;
          }
          if(ok) {
            maxCol++;
          }else{
            break;
          }
        }
      }
      for(int row = minRow; row <= maxRow; row++) {
        for(int col = minCol; col <= maxCol; col++) {
          map[row][col] = c;
        }
      }
    }
  }
}

void solve() {
  greedy();
  greedy2(false);
  greedy2(true);

  for(int i = 0; i < R; i++){
    cout << map[i] << endl;
  }
}
int main() {
  int T;
  cin >> T;
  for(int tz = 1; tz <= T; tz++) {
    cout << "Case #" << tz << ":" << endl;
    cin >> R >> C;
    map = vector<string>(R);
    for(int i = 0; i < R; i++) {
      cin >> map[i];
    }
    solve();
  }
}
