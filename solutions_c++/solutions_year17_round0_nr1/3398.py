#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 1005

int solve(char *, int);

int main() {
  int s, k, a;
  char p[MAXN];
 
  scanf("%d", &s);
  for (int c = 1; c <= s; ++c) {
    scanf("%s %d", p, &k);
    printf("Case #%d: ", c);
    a = solve(p, k);
    if (a > -1) {
      printf("%d\n", a);
    } else {
      puts("IMPOSSIBLE");
    }
  }
  return 0;
}

int solve(char *p, int k) {
  int c = 0;
  for (int i = 0; i <= strlen(p) - k; ++i) {
    if (p[i] == '-') {
      ++c;
      for (int j = 0; j < k; ++j) {
        p[i + j] = p[i + j] == '-' ? '+' : '-';
      }
    }
  }
  for (int i = strlen(p) - k; i < strlen(p); ++i) {
    if (p[i] == '-') {
      return -1;
    }
  }
  return c;
}
