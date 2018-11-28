#include <cstdio>

using namespace std;

char s[25][26];int r, c;
void fill(int i, int j, int pj = -1) {
  if(pj != -1) s[i][j] = s[i][pj];
  if(j-1 != pj && j-1 >= 0 && j-1 < c && s[i][j-1] == '?') fill(i,j-1,j);
  if(j+1 != pj && j+1 >= 0 && j+1 < c && s[i][j+1] == '?') fill(i,j+1,j);
}

void fill2(int i, int pi = -1) {
  if(pi != -1) for(int j = 0; j < c; ++j) s[i][j] = s[pi][j];
  if(i-1 != pi && i-1 >= 0 && i-1 < r && s[i-1][0] == '?') fill2(i-1,i);
  if(i+1 != pi && i+1 >= 0 && i+1 < r && s[i+1][0] == '?') fill2(i+1,i);
}
int main() {
  int t; scanf("%d", &t);
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &r, &c);
    for(int i = 0; i < r; ++i) {
      scanf(" %s", s[i]);
      for(int j = 0; j < c; ++j)
        if(s[i][j] != '?') fill(i, j);
    }
    for(int i = 0; i < r; ++i)
      if(s[i][0] != '?')
        fill2(i);
    printf("Case #%d:\n", cas);
    for(int i = 0; i < r; ++i)
      printf("%s\n", s[i]);
  }

  return 0;
}