#include <cstdio>
//#define __STDC_FORMAT_MACROS
#include <cstdint>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int len, k;
char s[1002];

void flip_tail(int p) {
  for (int i=0; (p+i)<len && i<k; ++i) if (s[p+i] == '-') s[p+i] = '+'; else s[p+i] = '-';
}

bool is_tail_good(int p) {
  for (int i=p; i<len; ++i) if (s[i] == '-') return false;
  return true;
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=1; i<=n; ++i) {
    int res = 0;
    scanf("%s %d", s, &k);
    len = strlen(s);
    int j = 0;
    for (j=0; j<=len-k; ++j) if (s[j] == '-') {
      flip_tail(j);
      ++res;
    }
    printf("Case #%d: ", i);
    if (is_tail_good(j)) printf("%d\n", res);
    else printf("IMPOSSIBLE\n");
  }
}
