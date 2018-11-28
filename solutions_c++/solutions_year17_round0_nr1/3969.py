#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    char s[2000];
    i64 K;
    scanf("%s %lld", s, &K);
    i64 ans = 0;
    i64 len = strlen(s);
    for (i64 i = 0; i < len; i++) {
      if (i + K > len) {
        break;
      }
      if (s[i] == '-') {
        ans += 1;
        for (i64 j = 0; j < K; j++) {
          if (s[i+j] == '-')
            s[i+j] = '+';
          else
            s[i+j] = '-';
        }
      }
    }
    bool good = true;
    for (i64 i = 0; i < len; i++) {
      if (s[i] == '-') good = false;
    }
    if (good) {
      printf("Case #%lld: %lld\n", zz, ans);
    } else {
      printf("Case #%lld: IMPOSSIBLE\n", zz);
    }
  }
}
