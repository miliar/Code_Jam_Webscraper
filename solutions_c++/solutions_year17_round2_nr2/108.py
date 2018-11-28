#include <stdio.h>
#include <cassert>

char s[1001];

int findMust(int n) {
  if (n == 0 || s[0] == s[n-1]) return 0;
  for (int i = 1; i < n; ++i) {
    if (s[i] == s[i-1]) return i;
  }
  return -1;
}

int findFit(int n, char c) {
  assert(n > 0);
  if (s[0] != c && s[n-1] != c) return 0;
  for (int i = 1; i < n; ++i) {
    if (s[i] != c && s[i-1] != c)
      return i;
  }
  return n;
}

int findColor(int n, char c) {
  if (n == 0) return 0;
  for (int i = 0; i < n; ++i)
    if (s[i] == c) return i;
  return -1;
}

void insert(int pos, int n, char c) {
  for (int i = n; i > pos; --i)
    s[i] = s[i-1];
  s[pos] = c;
  s[n+1] = '\0';
}

bool check(int n) {
  if (s[0] == s[n-1]) return false;
  for (int i = 1; i < n; ++i)
    if (s[i] == s[i-1]) return false;
  return true;
}

int main() {
  int T;
  int N, R, O, Y, G, B, V;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
    if (O > B || G > R || V > Y) {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    B -= O;
    R -= G;
    Y -= V;
    for (int i = 0; i < R; ++i)
      s[i] = 'R';
    int n = R;
    for (int i = 0; i < Y; ++i) {
      int pos = findMust(n);
      if (pos == -1) {
        pos = findFit(n, 'Y');
      }
      insert(pos, n, 'Y');
      n += 1;
    }
    for (int i = 0; i < B; ++i) {
      int pos = findMust(n);
      if (pos == -1) {
        pos = findFit(n, 'B');
      }
      insert(pos, n, 'B');
      n += 1;
    }
    if (!check(n)) {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    if (O > 0) {
      int pos = findColor(n, 'B');
      if (pos == -1) {
        printf("Case #%d: IMPOSSIBLE\n", t);
        continue;
      }
      for (int i = 0; i < O; ++i) {
        insert(pos, n, 'O');
        insert(pos, n+1, 'B');
        n += 2;
      }
    }
    if (G > 0) {
      int pos = findColor(n, 'R');
      if (pos == -1) {
        printf("Case #%d: IMPOSSIBLE\n", t);
        continue;
      }
      for (int i = 0; i < G; ++i) {
        insert(pos, n, 'G');
        insert(pos, n+1, 'R');
        n += 2;
      }
    }
    if (V > 0) {
      int pos = findColor(n, 'Y');
      if (pos == -1) {
        printf("Case #%d: IMPOSSIBLE\n", t);
        continue;
      }
      for (int i = 0; i < V; ++i) {
        insert(pos, n, 'V');
        insert(pos, n+1, 'Y');
        n += 2;
      }
    }
    s[N] = '\0';
    printf("Case #%d: %s\n", t, s);
  }
  return 0;
}
