#include <stdio.h>

char s[30][30];

int main(){
  int T;
  scanf("%d", &T);
  for(int tc=1; tc<=T; tc++){
    int R, C;
    scanf("%d%d", &R, &C);
    for(int i=0; i<R; i++) scanf("%s", s[i]);
    printf("Case #%d:\n", tc);
    for(int i=0; i<R; i++){
      for(int j=0; j<C; j++){
        if(s[i][j] != '?'){
          for(int a=1; a<=j; a++){
            if(s[i][j-a] == '?') s[i][j-a] = s[i][j];
            else break;
          }
        }
      }
    }
    for(int i=0; i<R; i++){
      for(int j=1; j<C; j++){
        if(s[i][j] == '?') s[i][j] = s[i][j-1];
      }
    }
    for(int i=1; i<R; i++){
      for(int j=0; j<C; j++){
        if(s[i][j] == '?') s[i][j] = s[i-1][j];
      }
    }
    for(int i=R-2; i>=0; i--){
      for(int j=0; j<C; j++){
        if(s[i][j] == '?') s[i][j] = s[i+1][j];
      }
    }
    for(int i=0; i<R; i++) printf("%s\n", s[i]);
  }
}
