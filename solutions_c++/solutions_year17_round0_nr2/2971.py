#include <cstdio>
#include <cstring>

using namespace std;

char buf[1002], *s = &buf[1];

int main() {
  int t;
  scanf("%d\n", &t);
  for (int it=1; it<=t; ++it) {
    char *r = s;
    scanf("%s", s);
    int len = strlen(s);
    for (int i=0; i<len; ++i) {
      if (s[i-1] <= s[i]) continue;
      for (int j=i-1; j>=0; --j) {
        if (s[j-1] < s[j]) {
          s[j]--;
          for (int k=j+1; k<len; ++k) s[k] = '9';
          break;
        }
      }
      break;
    }
    if (s[0] == '0') r = &s[1];
    printf("Case #%d: %s\n", it, r);
  }
}
