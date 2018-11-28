#include <bits/stdc++.h>

int N;
int E[101]; // max total distance
int S[101]; // top speed
int P[101][101];

float D[101][101]; // min time

int XX[101]; // 

bool volte[101];
void bejar(int A) {
  //printf("\n");
  for (int i = 1; i <= N; i++) volte[i] = false;
  for (int i = 1; i <= N; i++) XX[i] = 0;
  std::priority_queue<std::pair<float,int>> Q; // -s, a
  Q.push({-0, A});
  D[A][A] = 0;
  while (!Q.empty()) {
    auto x = Q.top();
    Q.pop();
    int a = x.second;
    int s = -x.first;
    if (volte[a]) continue;
    //printf("%d %d %d\n", a, s, XX[a]);
    volte[a] = true;
    for (int b = 1; b <= N; b++) {
      if (P[a][b] == -1) continue;
      int top_speed = S[A];
      int length = P[a][b];
      float ss = (float)length/top_speed;
      ss += D[A][a];
      /*printf("From %d to %d through %d S%d, V%d, T%f\n",
        A,b,a, length, top_speed, ss);
      printf("Old value %f, %d/%d\n",
        D[A][b], XX[a] + length, E[A]);*/
      if (ss < D[A][b] && XX[a] + length <= E[A]) {
//        printf("OK\n");
        XX[b] = XX[a] + length;
        D[A][b] = ss;
        Q.push({-ss, b});
      }
    }
  }
  for (int k = 1; k <= N; k++) {
    for (int i = 1; i <= N; i++) {
      if (i == k) continue;
      for (int j = 1; j <= N; j++) {
        if (j == i || j == k) continue;
        if (D[i][j] > D[i][k] + D[k][j]) {
          D[i][j] = D[i][k] + D[k][j];
        }
      }
    }
  }
   /* for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        printf("%d ", P[i][j]);
      }
      printf("\n");
    }*/
}
// 1 112
// 0 121
// 

void p() {
  int Q;
  scanf("%d%d", &N, &Q);
  for (int i = 1; i <= N; i++)
    scanf("%d%d", E+i, S+i);
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++) {
      int x;
      scanf("%d", &x);
      D[i][j] = 1e300;
      P[i][j] = x;
    }
  
  for (int i = 1; i <= N; i++)
    bejar(i);
  for (int i = 0; i < Q; i++) {
    int U, V;
    scanf("%d%d", &U, &V);
    printf(" %f", D[U][V]);
  }
  printf("\n");
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d:", i);
    p();
  }
}
