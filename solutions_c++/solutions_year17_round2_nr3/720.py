#include <bits/stdc++.h>

using namespace std;


int main() {
  int T;
  double mat[100][100], dist[100], speed[100];

  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    int N, Q;
    cin >> N >> Q;
    for(int i = 0; i < N; i++) {
      cin >> dist[i] >> speed[i];
    }

    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        double aux;
        cin >> aux;
        if(aux < 0)
          aux = HUGE_VAL;
        mat[i][j] = aux;
      }
      mat[i][i] = 0;
    }

    for(int k = 0; k < N; k++) {
      for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
          mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j]);
        }
      }
    }

    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        if(mat[i][j] > dist[i])
          mat[i][j] = HUGE_VAL;
        else
          mat[i][j] = mat[i][j]/speed[i];
      }
      mat[i][i] = 0;
    }

    for(int k = 0; k < N; k++) {
      for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
          mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j]);
        }
      }
    }

    cout << "Case #" << caso << ":";
    for(int i = 0; i < Q; i++) {
      int a, b;
      cin >> a >> b;
      printf(" %.7f", mat[a-1][b-1]);
    }
    cout << endl;
  }

  return 0;
}
