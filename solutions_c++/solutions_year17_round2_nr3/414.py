#include <iostream>
#include <stdio.h>
using namespace std;

long long D[200][200];
double T[200][200];
long long E[200], S[200], N, Q, u, v;
int main()
{
  int numTests;
  cin >> numTests;
  for (int test = 1; test <= numTests; test++) {
    cin >> N >> Q;
    for (int i = 1; i <= N; i++)
      cin >> E[i] >> S[i];
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= N; j++) {
        cin >> D[i][j];
      }
    for (int k = 1; k <= N; k++)
      for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
          if ((D[i][k] >= 0) && (D[k][j] >= 0) && ((D[i][k] + D[k][j] < D[i][j]) || (D[i][j] < 0)))
            D[i][j] = D[i][k] + D[k][j];

    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= N; j++) {
        T[i][j] = -1;
        if ((D[i][j] >= 0) && (D[i][j] <= E[i]))
          T[i][j] = D[i][j] / ((double)S[i]);
      }

    for (int k = 1; k <= N; k++)
      for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
          if ((T[i][k] >= 0) && (T[k][j] >= 0) && ((T[i][k] + T[k][j] < T[i][j]) || (T[i][j] < 0)))
            T[i][j] = T[i][k] + T[k][j];

    cout << "Case #" << test << ":";
    for (int i = 1; i <= Q; i++) {
      cin >> u >> v;
      printf(" %.8lf", T[u][v]);
    }
    cout << endl;
  }
}
