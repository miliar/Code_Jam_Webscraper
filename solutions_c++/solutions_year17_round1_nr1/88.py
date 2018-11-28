#include <cstdio>

char s[30][30];

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int R, C; scanf("%d%d", &R, &C);
    for(int i = 0; i < R; i++) scanf("%s", s[i]);

    for(int i = 0; i < R; i++){
      for(int j = 1; j < C; j++){
        if(s[i][j] == '?') s[i][j] = s[i][j - 1];
      }
    }

    for(int i = 0; i < R; i++){
      for(int j = C - 2; j >= 0; j--){
        if(s[i][j] == '?') s[i][j] = s[i][j + 1];
      }
    }

    for(int i = 1; i < R; i++){
      if(s[i][0] == '?'){
        for(int j = 0; j < C; j++) s[i][j] = s[i - 1][j];
      }
    }

    for(int i = R - 2; i >= 0; i--){
      if(s[i][0] == '?'){
        for(int j = 0; j < C; j++) s[i][j] = s[i + 1][j];
      }
    }

    printf("Case #%d:\n", tt);

    for(int i = 0; i < R; i++) puts(s[i]);
  }
  return 0;
}
