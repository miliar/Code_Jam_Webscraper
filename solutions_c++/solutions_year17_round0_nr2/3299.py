#include <stdio.h>
#include <string.h>

int T;
char s[30];

void solve(int testcase, char s[]) {
  int i, j, k;

  for (i = strlen(s) - 1; i >= 1; i--) {
    int min = s[i];
    for (j = i - 1; j >= 0; j--) {
      if(min < s[j]) {
        s[i] = '9';
        s[i-1] = s[i-1] - 1;
        break;
      }
      min = s[j];
    }
  }

  if(s[0] <= '0') {
    printf("Case #%d: %s\n", testcase, s + 1);
  } else {
    printf("Case #%d: %s\n", testcase, s);
  }
}

int main() {
  int testcase;
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);

  scanf("%d", &T);

  for(testcase = 1; testcase <= T; testcase++) {
    scanf("%s", s);
    solve(testcase, s);
  }
}
