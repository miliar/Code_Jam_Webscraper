#include <stdio.h>

char s[1005];

int main(){
  int T;
  scanf("%d", &T);
  for(int tc=0; tc<T; tc++){
    scanf("%s", s);
    int K;
    scanf("%d", &K);
    int N;
    for(N=0; s[N]; N++);
    int res = 0;
    for(int i=0; i<N-K+1; i++){
      if(s[i] == '-'){
        for(int j=i; j<i+K; j++){
          if(s[j] == '+') s[j] = '-';
          else s[j] = '+';
        }
        res++;
      }
    }
    int valid = 1;
    for(int i=0; i<N; i++) if(s[i] == '-') valid = 0;
    printf("Case #%d: ", tc+1);
    if(valid) printf("%d\n", res);
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}
