#include<cstdio>
#include<cstring>

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int ncase = 0; ncase < ncases; ncase++) {
    char s[1005];
    int n, k;
    scanf("%s", s);
    n = strlen(s);
    scanf("%d", &k);
    int tot = 0;
    for (int i = 0; i < n-k+1; i++) {
      if (s[i] == '+')
        continue;
      tot++;
      for (int j = i; j < i+k; j++)
        s[j] = (s[j] == '-') ? '+' : '-';
      //printf("%s\n", s);
    }
    printf("Case #%d: ", ncase+1);
    bool ok = true;
    for (int i = n-k+1; i < n; i++)
      if (s[i] != '+') {
        ok = false;
        break;
      }
    if (ok)
      printf("%d\n", tot);
    else
      printf("IMPOSSIBLE\n");
  }
  return 0;
}

