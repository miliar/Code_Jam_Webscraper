#include<bits/stdc++.h>

using namespace std;

char ch[2222];

int main() {
  freopen("B-large (1).in", "r", stdin);
  freopen("B-large (1).out", "w", stdout);
  int T, cas = 1; scanf("%d", &T);
  while (T --) {
    scanf("%s", ch);
    int len = strlen(ch);
    printf("Case #%d: ", cas ++);
    if (len == 1) {
      puts(ch);
      continue;
    }
    for (int i = 0; i < len - 1; i ++) {
      if (ch[i] > ch[i + 1]) {
        while (i > 0 && ch[i] == ch[i - 1]) i --;
        ch[i] --;
        for (int j = i + 1; j < len; j ++) ch[j] = '9';
        break;
      }
    }
    if (ch[0] == '0') puts(ch + 1);
    else puts(ch);
  }
  return 0;
}
