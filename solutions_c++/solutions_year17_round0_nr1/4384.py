#include <bits/stdc++.h>

using namespace std;

const int N = 1005,
          INF = N * N;

char s[N];
int tmp[N];
int n, k;

int get() {
  for (int i = 0; i < n; ++i) {
    tmp[i] = s[i] == '+' ? 1 : 0;
  }
  
  int res = 0;
  for (int i = 0; i + k <= n; ++i) {
    if (!tmp[i]) {
      res++;
      for (int j = 0; j < k; ++j) {
        tmp[j + i] ^= 1;
      }
    }
  }
  
  for (int i = 0; i < n; ++i) {
    if (!tmp[i]) return INF;
  }

  return res;
}

int main()
{
  int tt;
  scanf("%d", &tt);

  for (int _t = 1; _t <= tt; ++_t) {
    scanf("%s %d", s, &k);

    ::n = strlen(s);

    assert(n < N);

    int res = get();
    reverse(s, s + n);
    res = min(res, get());

    printf("Case #%d: ", _t);
    if (res == INF) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", res);
    }
  }

  return(0);
}
