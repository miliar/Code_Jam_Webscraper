#include <iostream>
#include <string>

using namespace std;

int T, R, C;
string cake[30];

int minX[30], minY[30];
int maxX[30], maxY[30];

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void solve() {
  memset(minX, R, sizeof(minX));
  memset(minY, C, sizeof(minY));
  memset(maxX, 0, sizeof(maxX));
  memset(maxY, 0, sizeof(maxY));

  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (cake[i][j] == '?') {
        continue;
      }
      int ix = cake[i][j] - 'A';
      minX[ix] = min(minX[ix], i);
      minY[ix] = min(minY[ix], j);
      maxX[ix] = max(maxX[ix], i);
      maxY[ix] = max(maxY[ix], j);
    }
  }

  for (int k = 0; k < 26; ++k) {
    for (int i = minX[k]; i <= maxX[k]; ++i) {
      for (int j = minY[k]; j <= maxY[k]; ++j) {
        if (cake[i][j] == '?') {
          cake[i][j] = (char)('A' + k);
        } 
      }
    }
  }

  //
  for (int i = 0; i < R; ++i) {
    char ch = '?';
    for (int j = 0; j < C; ++j) {
      if (cake[i][j] == '?') {
        cake[i][j] = ch;
      } else {
        ch = cake[i][j];
      }
    }
    ch = '?';
    for (int j = C-1; j >= 0; --j) {
      if (cake[i][j] == '?') {
        cake[i][j] = ch;
      } else {
        ch = cake[i][j];
      } 
    }
  }

  for (int i = 0; i < C; ++i) {
    char ch = '?';
    for (int j = 0; j < R; ++j) {
      if (cake[j][i] == '?') {
        cake[j][i] = ch;
      } else {
        ch = cake[j][i];
      }
    }
    ch = '?';
    for (int j = R-1; j >= 0; --j) {
      if (cake[j][i] == '?') {
        cake[j][i] = ch;
      } else {
        ch = cake[j][i];
      }
    }
  }
}

void print() {
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      cout << cake[i][j];
    }
    cout << endl;
  }
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
      cin >> cake[i];
    }
    solve();
    cout << "Case #" << t << ":" << endl;
    print();
  }
  return 0;
}