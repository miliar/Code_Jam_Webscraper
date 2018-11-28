#include <bits/stdc++.h>
using namespace std;
char s[32];
int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    printf("Case #%d: ", cas);
    scanf("%s", s);
    int len = strlen(s);
    if (len == 1) {
      printf("%s\n", s);
    } else {
      int num = 0;
      for (int i = 1; i < len; ++i) {
	if (s[i] < s[i - 1]) {
	  num = i;
	  break;
	}
      }
      if (num == 0) {
	printf("%s\n", s);
      } else {
	for (int i = num; i < len; ++ i) {
	  s[i] = '9';
	}
	for (int i = num - 1; i >= 0; -- i) {
	  s[i] = s[i] - 1;
	  if (i > 0 && s[i] < s[i - 1]) {
	    s[i] = '9';
	  } else {
	    break;
	  }
	}
	int t = 0;
	while (s[t] == '0') t ++;
	printf("%s\n", s + t);
      }
    }
  }
  return 0;
}
