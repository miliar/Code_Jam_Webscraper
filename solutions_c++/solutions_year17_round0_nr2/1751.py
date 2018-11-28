#include <cstdio>

char a[22];

void proc(char *a) {
  int i;
  for (i = 0; a[i] <= a[i + 1]; ++i);
  if (!a[i + 1]) return;
  for (; a[i] == a[i - 1]; --i);
  --a[i];
  for (++i; a[i]; ++i) {
    a[i] = '9';
  }
}

int main() {
  int t;
  scanf("%d", &t);
  a[0] = '0';
  for (int ti = 0; ti < t; ++ti) {
    scanf("%s", a + 1);
    proc(a);
    int i;
    for (i = 0; a[i] == '0'; ++i);
    printf("Case #%d: %s\n", ti + 1, a + i);
  }
  return 0;
}
