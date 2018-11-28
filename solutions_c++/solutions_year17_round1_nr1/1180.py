#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char a[30][30];
int R,C;
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  for (int _ = 1; _ <= T; _ ++) {

    scanf("%d %d", &R, &C);
    for (int i = 0; i < R; i++)
      scanf("%s",a[i]);
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        if (a[i][j] == '?'){
          int k = j;
          while (k < C && a[i][k] == '?') k++;
          if (k < C)  a[i][j] = a[i][k];
        }
      }
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        if (a[i][j] == '?'){
          int k = j;
          while (k >=0 && a[i][k] == '?') k--;
          if (k >= 0)  a[i][j] = a[i][k];
        }
      }

    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        if (a[i][j] == '?'){
          int k = i;
          while (k >= 0 && a[k][j] == '?') k--;
          if (k >= 0)  a[i][j] = a[k][j];
        }
      }
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++) {
        if (a[i][j] == '?'){
          int k = i;
          while (k < R && a[k][j] == '?') k++;
          if (k < R)  a[i][j] = a[k][j];
        }
      }
    printf("Case #%d:\n", _);
    for (int i = 0; i < R; i ++)
      printf("%s\n", a[i]);
  }
  return 0;
}
