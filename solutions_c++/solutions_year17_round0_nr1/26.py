#include <cstdio>
#include <cstring>

char s[1010];

void flip(char &x){ x = (x == '-' ? '+' : '-'); }

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    printf("Case #%d: ", tt);

    int K; scanf("%s%d", s, &K);
    int L = strlen(s);

    int cnt = 0;
    for(int i = 0; i <= L - K; i++){
      if(s[i] == '-'){
        cnt++;
        for(int j = 0; j < K; j++) flip(s[i + j]);
      }
    }

    bool v = true;
    for(int i = L - K + 1; i < L; i++) if(s[i] == '-') v = false;

    if(!v) puts("IMPOSSIBLE");
    else printf("%d\n", cnt);
  }
  return 0;
}
