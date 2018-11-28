#include <bits/stdc++.h>
using namespace std;

int r, c;
char cake[30][30];
int firstC[30];

void process(int x) {
  for(int i = 0; i < firstC[x]; i++) {
    cake[x][i] = cake[x][firstC[x]];
  }
  int cur = firstC[x];
  for(int i = firstC[x] + 1; i < c; i++) {
    while(i < c && cake[x][i] == '?') {
      cake[x][i] = cake[x][cur];
      i++;
    }
    cur = i;
  }
}

int main() {
  int kase;
  scanf("%d", &kase);
  for(int k = 1; k <= kase; k++) {
    scanf("%d%d", &r, &c);
    for(int i = 0; i < r; i++) {
      scanf("%s", cake[i]);
    }
    int firstR = -1;
    for(int i = r - 1; i >= 0; i--) {
      firstC[i] = -1;
      for(int j = 0; j < c; j++) {
        if(cake[i][j] != '?') {
          firstC[i] = j;
          firstR = i;
          break;
        }
      }
      if(firstC[i] != -1) {
        process(i);
      }
    }
    for(int i = 0; i < firstR; i++) {
      for(int j = 0; j < c; j++) {
        cake[i][j] = cake[firstR][j];
      }
    }
    int cur = firstR;
    for(int i = firstR + 1; i < r; i++) {
      while(i < r && firstC[i] == -1) {
        for(int j = 0; j < c; j++) {
          cake[i][j] = cake[cur][j];
        }
        i++;
      }
      cur = i;
    }
    printf("Case #%d:\n", k);
    for(int i = 0; i < r; i++) {
      for(int j = 0; j < c; j++) {
        printf("%c", cake[i][j]);
      }
      puts("");
    }
  }
  return 0;
}
