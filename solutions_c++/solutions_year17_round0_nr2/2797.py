#include <cstdio>

int main() {
  int N;
  scanf("%d", &N);
  char s[101];
  for (int i = 0; i < N; ++i) {
    scanf("%100s", s);
    int j = 1;
    while (s[j] && s[j] >= s[j - 1])
      ++j;
    if (s[j]) {
      j -= 2;
      while (j >= 0 && s[j] == s[j + 1]) {
        --j;
      }
      --s[j + 1];
      j += 2;
      while (s[j]) {
        s[j++] = '9';
      }
    }
    j = 0;
    while (s[j] == '0') {
      ++j;
    }
    printf("Case #%d: %s\n", i + 1, s + j);
  }
  return 0;
}
