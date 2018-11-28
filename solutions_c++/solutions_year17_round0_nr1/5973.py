#include <cstdio>
#include <cstring>

#define MAX_S 1005

int T, K;
char S[MAX_S];

bool check() {
  for (int i=0; i<=strlen(S); i++) {
    if (S[i] == '-')
      return false;
  }
  return true;
}

void solve () {
  int cnt = 0;
  //printf("[%s %d]", S, cnt);

  for (int i=0; i<=strlen(S)-K; i++) {
    if (S[i] == '-') {
      cnt++;
      for (int j=i; j<i+K; j++) {
        S[j] = S[j] == '-' ? '+' : '-';
      }
      //printf("[%s %d]", S, cnt);
    }
  }

  if (check()) {
    printf("%d\n", cnt);
  } else {
    printf("IMPOSSIBLE\n");
  }
}

int main () {
  scanf("%d", &T);

  for (int t=1; t<=T; t++) {
    printf("Case #%d: ", t);
    scanf("%s %d", S, &K);
    solve();
  }

  return 0;
}
