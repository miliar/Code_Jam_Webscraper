#include <bits/stdc++.h>

long long int solve(long long int n)
{
  int i, m = 0;
  char x = '0';
  char v = '0';
  char c[19] = {};
  char r[19] = {};

  sprintf(c, "%lld", n);

 r1:
  for(i=0; i<strlen(c); i++) {
    v = c[i];
    if(x > v) {
      m = i;
      break;
    }
    x = v;
  }

  if(m) {
    c[m - 1]--;
    for(i=m; i<strlen(c); i++) {
      c[i] = '9';
    }
    m = 0;
    x = '0';
    v = '0';
    goto r1;
  }

  return atoll(&c[0]);
}

int main(void)
{
  int T, C;

  scanf("%d", &T);
  for(C=1; C<=T; C++) {
    long long int N, X;
    scanf("%lld", &N);
    X = solve(N);

    printf("Case #%d: %lld\n", C, X);
  }

  return 0;
}
