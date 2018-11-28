#include <bits/stdc++.h>

using namespace std;

const int N = 100;

char s[N];
char res[N];
int n;

bool check(int pos, char u) {
  for (int i = pos; i <= n; i++) {
    res[i] = u;
  }
  for (int i = 1; i <= n; i++) {
    if (res[i] > s[i]) {
      return 0;
    }
    if (res[i] < s[i]) {
      return 1;
    }
  }
  return 1;
}

int main() {
//  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
  int tc;
  scanf("%d", &tc);
  for (int test = 1; test <= tc; test++) {
    scanf("%s", s + 1);
    n = strlen(s + 1);
    for (int i = 1; i <= n; i++) {
      char u = '9';
      while (u >= '0') {
        if (check(i, u)) {
          break;
        }
        u--;
      }
    }
    printf("Case #%d: ", test);
    int f=  0;
    for (int i = 1; i <= n; i++) {
      if (res[i] == '0' && !f) {
        continue;
      }
      if (res[i] != '0') {
        f = 1;
      }
      putchar(res[i]);
    }
    printf("\n");
  }
  return 0;
}
