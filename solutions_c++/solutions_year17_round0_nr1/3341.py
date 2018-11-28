#include <stdio.h>
#include <string.h>

int T;
char s[10000];
int k;

int solve(int testcase, char s[], int k) {
  int i, ans = 0, j;
  for (i = 0; i < strlen(s); i++) {
    if(s[i] == '-') {
      if(i + k - 1 >= strlen(s)) return -1;
      for(j = i; j <= i + k - 1; j++) {
        if(s[j] == '-') s[j] = '+';
        else if(s[j] == '+') s[j] = '-';
      }
      ans = ans + 1;
    }
  }
  return ans;
}

int main() {
  int testcase;
  freopen("aa.in", "r", stdin);
  freopen("aa.out", "w", stdout);

  scanf("%d", &T);

  for(testcase = 1; testcase <= T; testcase++) {
    scanf("%s", s);
    scanf("%d", &k);
    int ans = solve(testcase, s, k);
    if (ans < 0) printf("Case #%d: IMPOSSIBLE\n", testcase);
    else printf("Case #%d: %d\n", testcase, ans);
  }
}
