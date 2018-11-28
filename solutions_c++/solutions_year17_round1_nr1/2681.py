#include<stdio.h>
char s[1000][1000];
int fill(int x1, int y1, int x2, int y2, char c) {
  for(int i = x1 ; i <= x2; i++) {
    for(int j = y1 ; j <= y2 ; j++) {
      s[i][j]  = c;
    }
  }
}

int main(){
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e< t ;e++) {
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i = 0 ; i < n ; i++) {
      scanf("%s", s[i]);
    }
    int fr = 0, lr = 0;
    for(int i = 0 ; i < n ; i++ ) {
      int found = 0;
      int pc = 0;
      char late ;
      for(int j = 0; j < m ; j++ ) {
        if (s[i][j] != '?') {
          found = 1;
          fill(fr, pc, lr, j, s[i][j]);
          pc = j+1;
          late = s[i][j];
        }
        else if (j == m-1 && found) {
          fill(fr, pc, lr, j, late);
        }
      }
      if (found) {
        fr = i+1;
      }
      lr++;
    }
    if (fr < n) {
      for(int i = fr ; i < n ; i++) {
        for(int j = 0 ; j < m ; j++) {
          s[i][j] = s[i-1][j];
        }
      }
    }
    printf("Case #%d:\n", e+1);
    for(int i = 0 ; i < n ; i++) {
      printf("%s\n",s[i]);
    }
  }
}
