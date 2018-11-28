#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

char s[100][100];
int r, c;

int main() {
  int T, cas = 0;
  scanf("%d", &T);
  while (T--) {
    printf("Case #%d:\n", ++cas);
    memset(s, 0, sizeof(s));
    scanf("%d%d", &r, &c);
    gets(s[0]);
    for (int i = 0; i < r; ++i) {
      gets(s[i]);
    }
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (s[i][j] != '?') {
          for (int k = j-1; k >= 0 && s[i][k] == '?'; --k) {
            s[i][k] = s[i][j];
          }
          for (int k = j+1; k < c && s[i][k] == '?'; ++k) {
            s[i][k] = s[i][j];
          }
        }
      }
    }
    for (int i = 0; i < r; ++i) {
      if (s[i][0] != '?') {
        for (int k = i - 1; k >= 0 && s[k][0] == '?'; --k) {
          for (int j = 0; j < c; ++j) {
            s[k][j] = s[i][j];
          }
        }
        for (int k = i + 1; k < r && s[k][0] == '?'; ++k) {
          for (int j = 0; j < c; ++j) {
            s[k][j] = s[i][j];
          }
        }
      }
    }
    for (int i = 0; i < r; ++i) puts(s[i]);
  }
  return 0;
}
