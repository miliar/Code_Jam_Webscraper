// C++11
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int R, C; scanf("%d%d", &R, &C);
    char table[30][30];
    for(int i = 0; i < R; ++i) {
      scanf(" %s", table[i]);
    }
    for(int i = 0; i < R; ++i) {
      int lastj = 0;
      char lastch = '?';
      for(int j = 0; j <= C; ++j) {
        if(j < C && table[i][j] == '?') continue;
        if(j < C) lastch = table[i][j];
        for(int jj = lastj; jj <= j; ++jj) {
          if(jj < C) table[i][jj] = lastch;
        }
        lastj = j + 1;
      }
    }
    for(int j = 0; j < C; ++j) {
      int lasti = 0;
      char lastch = '?';
      for(int i = 0; i <= R; ++i) {
        if(i < R && table[i][j] == '?') continue;
        if(i < R) lastch = table[i][j];
        for(int ii = lasti; ii <= i; ++ii) {
          if(ii < R) table[ii][j] = lastch;
        }
        lasti = i + 1;
      }
    }
    printf("Case #%d:\n", tci+1);
    for(int i = 0; i < R; ++i) {
      printf("%s\n", table[i]);
    }
  }
  return 0;
}
