#include <bits/stdc++.h>
using namespace std;

char MAP[26][26];

int main(void) {

  int cases; scanf("%d", &cases);
  for (int cas = 1; cas <= cases; ++cas) {
    printf("Case #%d:\n", cas);
    int R, C; scanf("%d %d", &R, &C);
    for (int i = 0; i < R; ++i) {
      scanf(" %s", MAP[i]);
    }

    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (MAP[i][j] != '?') {
          for (int k = j-1; k >= 0 && MAP[i][k] == '?'; --k) {
            MAP[i][k] = MAP[i][j];
          }
          for (int k = j+1; k < C && MAP[i][k] == '?'; ++k) {
            MAP[i][k] = MAP[i][j];
          }
        }
      }
    }

    for (int i = 0; i < R; ++i) {
      if (MAP[i][0] != '?') {
        for (int j = i-1; j >= 0 && MAP[j][0] == '?'; --j) {
          for (int k = 0; k < C; ++k) {
            MAP[j][k] = MAP[i][k];
          }
        }
        for (int j = i+1; j < R && MAP[j][0] == '?'; ++j) {
          for (int k = 0; k < C; ++k) {
            MAP[j][k] = MAP[i][k];
          }
        }
      }
    }
    for (int i = 0; i < R; ++i) {
      printf("%s\n", MAP[i]);
    }
  }

  return 0;
}