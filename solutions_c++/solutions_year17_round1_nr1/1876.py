#include <stdio.h>

int T, r, c;
char A[30][30];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; ++t) {
    scanf("%d%d", &r, &c);
    for (int i = 0 ; i < r ; ++i) {
      scanf("%s", A[i]);
    }

    for (int i = 0 ; i < r ; ++i) {
      for (int j = 1 ; j < c ; ++j) {
        if (A[i][j - 1] != '?' && A[i][j] == '?') {
          A[i][j] = A[i][j - 1];
        }
      }
      for (int j = c - 2 ; j >= 0 ; --j) {
        if (A[i][j + 1] != '?' && A[i][j] == '?') {
          A[i][j] = A[i][j + 1];
        }
      }
    }

    for (int i = 1 ; i < r ; ++i) {
      for (int j = 0 ; j < c ; ++j) {
        if (A[i][j] == '?') {
          A[i][j] = A[i - 1][j];
        }
      }
    }

    for (int i = r - 2 ; i >= 0 ; --i) {
      for (int j = 0 ; j < c ; ++j) {
        if (A[i][j] == '?') {
          A[i][j] = A[i + 1][j];
        }
      }
    }

    printf("Case #%d:\n", t);
    for (int i = 0 ; i < r ; ++i) {
      printf("%s\n", A[i]);
    }
  }
}