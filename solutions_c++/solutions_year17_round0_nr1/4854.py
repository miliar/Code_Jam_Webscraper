#include <cstdio>
#include <cstring>

int T, tt;
char a[5000];
int k;

void flip(int i) {
  for(int j = i; j < i + k; j++) {
    if(a[j] == '-')
      a[j] = '+';
    else
      a[j] = '-';
  }
}

int solve() {
  scanf("%s %d", a, &k);
  int len = strlen(a);
  int count = 0;
  for(int i = 0; i < len; i++) {
    if(a[i] == '-') {
      if(i + k > len)
        return -1;
      else
        flip(i);
      count++;
    }
    else
      continue;
  }
  return count;
}

int main() {
  scanf("%d", &T);
  for(tt = 1; tt <= T; tt++) {
    printf("Case #%d: ", tt);
    int res = solve();
    if(res < 0)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", res);
  }
  return 0;
}
