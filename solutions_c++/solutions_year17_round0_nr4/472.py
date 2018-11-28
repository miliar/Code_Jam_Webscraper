#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

const int EMPTY = 0;
const int INIT = 1;
const int PLACED = 2;
const int FILLED = 3;

int N;
int hori[100][100];
int diag[100][100];

int DR[4] = { -1, -1,  1, 1 };
int DC[4] = { -1,  1, -1, 1 };

void putHori(int r, int c, bool init) {
  hori[r][c] = init ? INIT : PLACED;
  for(int k = 0; k < 4; ++k) {
    int nr = r, nc = c;
    for(int i = 0; i < N; ++i) {
      nr += DR[k], nc += DC[k];
      if(nr < 0 || nc < 0 || N <= nr || N <= nc) break;
      hori[nr][nc] = FILLED;
    }
  }
}

void putDiag(int r, int c, bool init) {
  for(int i = 0; i < N; ++i) {
    int nr = (r + i) % N, nc = (c + i) % N;
    diag[nr][c] = diag[r][nc] = FILLED;
  }
  diag[r][c] = init ? INIT : PLACED;
}

void solveHori() {
  for(int i = 0; i < N; ++i) {
    if(hori[i][0] == EMPTY) putHori(i, 0, false);
    if(hori[i][N-1] == EMPTY) putHori(i, N-1, false);
    if(hori[0][i] == EMPTY) putHori(0, i, false);
    if(hori[N-1][i] == EMPTY) putHori(N-1, i, false);
  }
}

void solveDiag() {
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j < N; ++j) {
      if(diag[i][j] == EMPTY) {
        putDiag(i, j, false);
        break;
      }
    }
  }
}

int main(void){
  int T, M;
  cin >> T;
  for(int tt = 0; tt < T; ++tt) {
    cin >> N >> M;
    for(int i = 0; i < N; ++i) {
      fill_n(hori[i], N, EMPTY);
      fill_n(diag[i], N, EMPTY);
    }
    for(int i = 0; i < M; ++i) {
      int r, c;
      char ch;
      cin >> ch >> r >> c;
      --r, --c;
      if(ch == '+' || ch == 'o') putHori(r, c, true);
      if(ch == 'x' || ch == 'o') putDiag(r, c, true);
    }

    solveHori();
    solveDiag();

    int x = 0, y = 0;
    for(int i = 0; i < N; ++i)
      for(int j = 0; j < N; ++j) {
        if(hori[i][j] == INIT || hori[i][j] == PLACED) ++x;
        if(diag[i][j] == INIT || diag[i][j] == PLACED) ++x;
        if(hori[i][j] == PLACED || diag[i][j] == PLACED) ++y;
      }
    cout << "Case #" << tt+1 << ": " << x << ' ' << y << endl;
    for(int i = 0; i < N; ++i)
      for(int j = 0; j < N; ++j)
        if(hori[i][j] == PLACED || diag[i][j] == PLACED) {
          if((hori[i][j] == PLACED || hori[i][j] == INIT) &&
             (diag[i][j] == PLACED || diag[i][j] == INIT))
            cout << 'o';
          else if(hori[i][j] == PLACED || hori[i][j] == INIT)
            cout << '+';
          else
            cout << 'x';
          cout << ' ' << i+1 << ' ' << j+1 << endl;
        }
  }

  return 0;
}
