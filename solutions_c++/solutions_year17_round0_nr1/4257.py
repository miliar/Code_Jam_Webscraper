#include <bits/stdc++.h>
using namespace std;
char s[1024];
int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    scanf("%s", s);
    int len = strlen(s);
    int n;
    scanf("%d", &n);
    int num = 0;
    for (int i = 0; i <= len - n; ++ i) {
      if (s[i] == '-') {
	num ++;
	for (int j = 0; j < n; ++ j) {
	  if (s[i + j] == '-') s[i + j] = '+';
	  else s[i + j] = '-';
	}
      }
    }
    int tag = true;
    for (int i = 0; i < len; ++ i) {
      if (s[i] == '-') {
	tag = false;
	break;
      }
    }
    if (tag) {
      printf("Case #%d: %d\n", cas, num);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", cas);
    }
  }
  return 0;
}
