#include <bits/stdc++.h>
using namespace std;

void solve(char *N, bool m) {
  if (m) N[0] = '9';
  if (!N[1]) return;
  if (!m && N[0] > N[1]) {
    N[0] = N[0]-1;
    N[1] = '9';
    m = 1;
  }
  solve(N+1, m);
  if (N[0] > N[1]) {
    N[0] = N[0]-1;
    N[1] = '9';
  }
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w+", stdout);
  int T, l;
  char N[30];
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", N);
    solve(N, 0);
    printf("Case #%d: ", t);
    for (int i = 0; N[i]; i++) {
      if (N[i] == '0') continue;
      printf("%s\n", N+i);
      break;
    }
  }
  
  return 0;
}

