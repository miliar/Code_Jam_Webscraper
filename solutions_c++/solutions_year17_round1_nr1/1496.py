#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

char ma[26][26];

int main() {
  int t;
  int r, c;

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; i++) {
      scanf("%s", ma[i]);
    }
    for (int i = 0; i < r; i++) {
      int f = 0;
      for (int j = 0; j < c; j++) {
        if (ma[i][j] != '?') {
          f = ma[i][j];
          break;
        }
      }
      if (f == 0) {
        continue;
      }
      for (int j = 0; j < c; j++) {
        if (ma[i][j] != '?') {
          f = ma[i][j];
        } else {
          ma[i][j] = f;
        }
      }
    }
    for (int j = 0; j < c; j++) {
      int f = 0;
      for (int i = 0; i < r; i++) {
        if (ma[i][j] != '?') {
          f = ma[i][j];
          break;
        }
      }
      for (int i = 0; i < r; i++) {
        if (ma[i][j] != '?') {
          f = ma[i][j];
        } else {
          ma[i][j] = f;
        }
      }
    }

    printf("Case #%d:\n", o + 1);
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        printf("%c", ma[i][j]);
      }
      printf("\n");
    }
  }

  return 0;
}
