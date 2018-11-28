#include<bits/stdtr1c++.h>
using namespace std;

int T, R, C;

vector<string> A;
vector<vector<int> > D;
const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};

char search(int x, int y) {
  if (A[x][y] != '?') {
    return A[x][y];
  }
  return A[x][y] = search(x + dx[D[x][y]], y + dy[D[x][y]]);
}

int main () {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ":" << endl;
    cin >> R >> C;
    A.resize(R);
    D = vector<vector<int> >(R, vector<int>(C));
    for (int i = 0; i < R; ++i) {
      cin >> A[i];
    }
    bool rows = false;
    for (int i = 0; i < R; ++i) {
      bool rseen = false;
      for (int j = 0; j < C; ++j) {
        rseen |= A[i][j] != '?';
      }
      if (rseen) {
        rows = true;
        bool cols = false;
        for (int j = 0; j < C; ++j) {
          if (A[i][j] == '?') {
            if (cols) {
              D[i][j] = 3;
            } else {
              D[i][j] = 2;
            }
          } else {
            cols = true;
          }
        }
      } else {
        int dir;
        if (rows) {
          dir = 1;
        } else {
          dir = 0;
        }
        for (int j = 0; j < C; ++j) {
          D[i][j] = dir;
        }
      }
    }
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        search(i, j);
      }
    }
    for (int i = 0; i < R; ++i) {
      cout << A[i] << endl;
    }
  }

  return 0;
}
