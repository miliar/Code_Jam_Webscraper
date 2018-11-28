#include <cstdio>
#include <algorithm>

using namespace std;

char s[1111];

int main(void) {
  int T; scanf("%d", &T);
  for (int ijk = 1; ijk <= T; ijk++) {
    int k, len; scanf("%s%d", s, &k);
    for (len = 0; s[len]; len++);

    int res = 0;
    for (int i = 0; i+k-1 < len; i++) {
      if (s[i] == '-') {
        ++res;
        for (int j = 0; j < k; j++) {
          s[i+j] = (s[i+j] == '-' ? '+' : '-');
        }
      }
    }
    printf("Case #%d: ", ijk);
    if (all_of(s, s+len, [](char c) {return c == '+';})) printf("%d\n", res);
    else puts("IMPOSSIBLE");
  }
  return 0;
}
