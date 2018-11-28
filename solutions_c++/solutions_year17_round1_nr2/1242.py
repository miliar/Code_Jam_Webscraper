#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>

void print(int caseNum, int output) {
  std::cout << "Case #" << caseNum << ": " << output << std::endl;
}

int *intersect(int n1, int p1, int n2, int p2, int lower[][50], int upper[][50]) {
  if (lower[n1][p1] > upper[n2][p2] || lower[n2][p2] > upper[n1][p1]) return NULL;

  int result[2];
  result[0] = std::max(lower[n1][p1], lower[n2][p2]);
  result[1] = std::min(upper[n1][p1], upper[n2][p2]);
  return result;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    int N, P;
    scanf("%d %d", &N, &P);

    int R[50];
    for (int n = 0; n < N; ++n) {
      scanf("%d", &R[n]);
    }

    int Q[50][50];
    for (int n = 0; n < N; ++n) {
      for (int p = 0; p < P; ++p) {
        scanf("%d", &Q[n][p]);
      }
      std::sort(Q[n], Q[n]+P);
    }

    int lower[50][50];
    int upper[50][50];
    for (int n = 0; n < N; ++n) {
      int amount = R[n];
      for (int p = 0; p < P; ++p) {
        lower[n][p] = ceil(Q[n][p] / (1.1*amount));
        upper[n][p] = floor(Q[n][p] / (0.9*amount));
      }
    }

    // small

    int count = 0;
    int Nind[50] = {};
    if (N == 1) {
      while (Nind[0] < P) {
        if (lower[0][Nind[0]] > upper[0][Nind[0]]) {
          Nind[0]++;
          continue;
        }
        Nind[0]++;
        count++;
      }
    } else {
      while (Nind[0] < P && Nind[1] < P) {
        if (lower[0][Nind[0]] > upper[0][Nind[0]]) {
          Nind[0]++;
          continue;
        }
        if (lower[1][Nind[1]] > upper[1][Nind[1]]) {
          Nind[1]++;
          continue;
        }
        int *share = intersect(0, Nind[0], 1, Nind[1], lower, upper);
        if (share == NULL) {
          if (lower[0][Nind[0]] < lower[1][Nind[1]]) Nind[0]++;
          else Nind[1]++;
        } else {
          Nind[0]++;
          Nind[1]++;
          count++;
        }
      }
    }

    print(t, count);
  }

  return 0;
}
