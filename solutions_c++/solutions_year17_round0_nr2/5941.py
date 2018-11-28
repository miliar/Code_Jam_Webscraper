#include <cstdio>
#include <cstring>

#define MAX 20

int T;
char N[MAX];

void solve() {
  int lar = 0, idx = -1;

  for (int i=0; i<strlen(N); i++) {
    if (N[i] > lar) {
      lar = N[i];
      idx = i;
    } else if (N[i] < lar) {
      for (int j=0; j<idx; j++)
        printf("%c", N[j]);
      if (lar > '1')
        printf("%c", lar-1);
      for (int j=0; j<strlen(N)-(idx+1); j++)
        printf("9");
      printf("\n");
      return;
    }
  }

  printf("%s\n", N);
}

int main() {
  scanf("%d", &T);

  for (int t=1; t<=T; t++) {
    printf("Case #%d: ", t);
    scanf("%s", N);
    solve();
  }

  return 0;
}
