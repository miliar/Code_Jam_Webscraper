#include <cstdio>
#include <cstring>

const int MAX_LENGTH = 1000;

int main(void) {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    int k;
    char s[MAX_LENGTH + 1];
    scanf("%s %d", s, &k);
    int n = strlen(s);
    int answer = 0;
    for (int i = 0; i + k - 1 < n; i++) {
      if (s[i] == '-') {
        answer++;
        for (int j = 0; j < k; j++) {
          if (s[i + j] == '+')
            s[i + j] = '-';
          else
            s[i + j] = '+';
        }
      }
    }
    int i = 0;
    while (i < n && s[i] == '+')
      i++;
    if (i < n)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", answer);
  }
  return 0;
}
