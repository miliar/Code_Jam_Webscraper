#include <cstdio>
#include <cstring>

const int N = 1111;

int n, k;
char s[N];

char toggle(char c) {
  return c == '-' ? '+' : '-';
}

int main() {
  int tt;
  scanf("%d", &tt);
  for(int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    scanf("%s%d", s, &k);
    n = strlen(s);
    int ans = 0;
    for(int i = 0; i < n - k + 1; i++) {
      if(s[i] == '-') {
        for(int j = 0; j < k; j++) {
          s[i+j] = toggle(s[i+j]);
        }
        ans ++;
      }
    }
    for(int i = 0; i < n; i++)
      if(s[i] != '+')
        ans = -1;
    if(ans != -1)
      printf("%d\n", ans);
    else
      printf("IMPOSSIBLE\n");
  }
}
