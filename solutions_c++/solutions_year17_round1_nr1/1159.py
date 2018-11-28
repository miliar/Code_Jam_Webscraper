#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

const int MAXN = 30;

string mat[MAXN];
int cnt[MAXN];
int l[MAXN], r[MAXN], t[MAXN], b[MAXN];

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    int N, M;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
      cin >> mat[i];
    }
    for (int i = 0; i < MAXN; ++i) cnt[i] = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        if (mat[i][j] != '?') {
          cnt[mat[i][j] - 'A']++;
        }
      }
    }
    for (int c = 0; c < MAXN; ++c) {
      if (cnt[c] != 0) {
        l[c] = M, r[c] = -1, t[c] = N, b[c] = -1;
        for (int i = 0; i < N; ++i) {
          for (int j = 0; j < M; ++j) {
            if (mat[i][j] - 'A' == c) {
              l[c] = min(l[c], j);
              r[c] = max(r[c], j);
              t[c] = min(t[c], i);
              b[c] = max(b[c], i);
            }
          }
        }
        for (int i = t[c]; i <= b[c]; ++i) {
          for (int j = l[c]; j <= r[c]; ++j) {
            mat[i][j] = c + 'A';
          }
        }
      }
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        if (mat[i][j] != '?') {
          int c = mat[i][j] - 'A';
          int ll = l[c] - 1;
          while (ll >= 0) {
            bool allEmpty = true;
            for (int k = t[c]; k <= b[c]; ++k) {
              if (mat[k][ll] != '?') {
                allEmpty = false;
              }
            }
            if (allEmpty) {
              for (int k = t[c]; k <= b[c]; ++k) {
                mat[k][ll] = c + 'A';
              }
              --l[c];
              --ll;
            } else {
              break;
            }
          }
          int rr = r[c] + 1;
          while (rr < M) {
            bool allEmpty = true;
            for (int k = t[c]; k <= b[c]; ++k) {
              if (mat[k][rr] != '?') {
                allEmpty = false;
              }
            }
            if (allEmpty) {
              for (int k = t[c]; k <= b[c]; ++k) {
                mat[k][rr] = c + 'A';
              }
              ++r[c];
              ++rr;
            } else {
              break;
            }
          }
        }
      }
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        if (mat[i][j] != '?') {
          int c = mat[i][j] - 'A';
          int tt = t[c] - 1;
          while (tt >= 0) {
            bool allEmpty = true;
            for (int k = l[c]; k <= r[c]; ++k) {
              if (mat[tt][k] != '?') {
                allEmpty = false;
              }
            }
            if (allEmpty) {
              for (int k = l[c]; k <= r[c]; ++k) {
                mat[tt][k] = c + 'A';
              }
              --t[c];
              --tt;
            } else {
              break;
            }
          }
          int bb = b[c] + 1;
          while (bb < N) {
            bool allEmpty = true;
            for (int k = l[c]; k <= r[c]; ++k) {
              if (mat[bb][k] != '?') {
                allEmpty = false;
              }
            }
            if (allEmpty) {
              for (int k = l[c]; k <= r[c]; ++k) {
                mat[bb][k] = c + 'A';
              }
              ++b[c];
              ++bb;
            } else {
              break;
            }
          }
        }
      }
    }

    printf("Case #%d:\n", cases + 1);
    for (int i = 0; i < N; ++i) {
      cout << mat[i] << endl;
    }

  }
}