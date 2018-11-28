#include <cstdio>
#include <cstring>

static const int MX = 1007;

char S[MX];

bool fixed(int idx, int k, int n) {
  for (int i = idx; k > 0; --k, ++i) {
    if (i > n) 
      return false;
    if (S[i] == '+') S[i] = '-';
    else S[i] = '+';
  }
  return true;
}

void solve() {
  int counter = 0;
  int n, k;
  scanf(" %s %d", S + 1, &k);
  n = (int)strlen(S + 1);

  for (int i = 1; i <= n; ++i) {
    if (S[i] == '-') {
      if (fixed(i, k, n) == false) {
        puts("IMPOSSIBLE");
        return;
      } 
      ++counter;
    }
  }
  
  printf("%d\n", counter);
}


int main() {
  int qqq;
  scanf("%d", &qqq);
  
  for (int i = 1; i <= qqq; ++i) {
    printf("Case #%d: ", i); 
    solve();
  }

  return 0;
}
