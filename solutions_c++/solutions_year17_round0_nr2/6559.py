#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
  int t;
  char n[20];

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    scanf("%s", n);
    int l = strlen(n);
    int pos = l;
    for (int i = l - 2; i >=0; i--) {
      if (n[i] > n[i + 1]) {
        n[i] -= 1;
        pos = i + 1;
      }
    }
    for (int i = pos; i < l; i++) {
      n[i] = '9';
    }
    int i;
    for (i = 0; i < l; i++) {
      if (n[i] != '0') {
        printf("Case #%d: %s\n", o + 1, n + i);
        break;
      }
    }
    if (i == l) {
      printf("Case #%d: 0\n", o + 1);
    }
  }

  return 0;
}
