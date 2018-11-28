#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    int N, Q;
    cin >> N >> Q;

    long E[100] = { 0, };
    long S[100] = { 0, };
    long D[100][100] = { 0, };
    long U[100] = { 0, };
    long V[100] = { 0, };

    for (int i = 0; i < N; ++i) {
      cin >> E[i] >> S[i];
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        cin >> D[i][j];
      }
    }

    for (int i = 0; i < Q; ++i) {
      cin >> U[i] >> V[i];
    }

    double R[100][100] = { 0, };

    for (int i = 0; i < N; ++i) {
      int lala = E[i];
      for (int j = i + 1; j < N; ++j) {
        if (lala < D[j - 1][j])
          break;

        lala -= D[j - 1][j];
        R[i][j] = D[j - 1][j] * 1.0 / S[i];

        double mm = 0;

        if (j != i + 1)
          mm = R[i][j - 1];
        else {
          mm = DBL_MAX;

          for (int k = 0; k <= i; ++k) {
            if (R[k][j - 1] != 0 && mm > R[k][j - 1]) {
              mm = R[k][j - 1];
            }
          }
        }

        if (mm != DBL_MAX)
          R[i][j] += mm;
      }
    }

    double r = DBL_MAX;

    for (int i = 0; i < N; ++i) {
      if (R[i][N - 1] != 0 && r > R[i][N - 1])
        r = R[i][N - 1];
    }

    cout << "Case #" << t + 1 << ": " << fixed << setprecision(9) << r;

    cout << endl;
  }

  return 0;
}