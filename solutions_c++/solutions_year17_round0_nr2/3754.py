#include <bits/stdc++.h>

using namespace std;

void io() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

int len(char a[]) {
  int ret = 0;
  while (a[ret] != '\0') {
    ret++;
  }
  return ret;
}

int main() {
  io();
  int test, n, mark;
  char s[1234];
  scanf("%d", &test);
  for (int t = 1; t <= test; t++) {
    scanf("%s", s);
    n = len(s);
    mark = -1;
    for (int i = 1; i < n; i++) {
      if (s[i] < s[i - 1]) {
        mark = i - 1;
        break;
      }
    }
    while (mark - 1 >= 0 && s[mark] == s[mark - 1]) {
      mark--;
    }
    if (mark >= 0) {
      s[mark]--;
      for (int i = mark + 1; i < n; i++) {
        s[i] = '9';
      }
    }
    int i = 0;
    while (i < n && s[i] == '0') {
      i++;
    }
    printf("Case #%d: ", t);
    if (i == n) {
      printf("0\n");
    } else {
      for (; i < n; i++) {
        printf("%c", s[i]);
      }
      printf("\n");
    }
  }
  return 0;
}
