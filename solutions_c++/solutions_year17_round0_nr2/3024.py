#include <cstdio>

const int MAX_LENGTH = 19;

int main(void) {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    char s[MAX_LENGTH + 1];
    int n;
    scanf("%s", s);
    int i = 0;
    while (s[i + 1] != '\0' && s[i] <= s[i + 1])
      i++;
    if (s[i + 1] != '\0') {
      int j = i;
      while (j >= 0 && s[j] == s[i])
        j--;
      j++;
      s[j]--;
      j++;
      while (s[j] != '\0') {
        s[j] = '9';
        j++;
      }
    }

    if (s[0] == '0')
      printf("%s\n", s + 1);
    else
      printf("%s\n", s);
  }
  return 0;
}
