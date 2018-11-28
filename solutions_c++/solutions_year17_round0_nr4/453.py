#include <bits/stdc++.h>

using namespace std;

vector<vector<char>> mat, mat2;

int main() {
  int T;
  int N, M;
  cin >> T;

  for(int caso = 1; caso <= T; caso++) {
    cin >> N >> M;

    mat.assign(N+1, vector<char>(N+1, '.'));
    mat2.assign(N+1, vector<char>(N+1, '.'));
    int o = 0;

    for(int k = 0; k < M; k++) {
      char c;
      int i, j;
      cin >> c >> i >> j;
      mat[i][j] = c;
      if(c != '+') {
        o = j;
      }
    }

    int points = 0, changes = 0;

    if(!o) o = 1;
    for(int j = 1; j <= N; j++) {
      if(j != o) {
        if(mat[1][j] == '.')
          changes++;
        points++;
        mat2[1][j] = '+';
      }
    }
    if(mat[1][o] != 'o')
      changes++;
    points += 2;
    mat2[1][o] = 'o';

    if(o <= N/2) {
      int d = 1;
      for(int i = 2; i <= N; i++) {
        if(mat2[1][d] == 'o') d++;
        points++;
        changes++;
        mat2[i][d] = 'x';
        d++;
      }
    } else {
      int d = N;
      for(int i = 2; i <= N; i++) {
        if(mat2[1][d] == 'o') d--;
        points++;
        changes++;
        mat2[i][d] = 'x';
        d--;
      }
    }

    for(int j = 2; j < N; j++) {
      if(mat2[N][j] == '.') {
        mat2[N][j] = '+';
        points++;
        changes++;
      }
    }

    cout << "Case #" << caso << ": " << points << " " << changes << endl;
    for(int i = 1; i <= N; i++) {
      for(int j = 1; j <= N; j++)
        if(mat[i][j] != mat2[i][j]) {
          cout << mat2[i][j] << " " << i << " " << j << endl;
        }
    }

  }
  return 0;
}
