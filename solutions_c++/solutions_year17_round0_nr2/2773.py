#include <cstdio>
#include <cstring>

void solve(int test_id) {
  char t[100];
  char* a = t;
  scanf("%s", a);
  int N = strlen(a), idx = 0;

  for (;idx < N - 1; ++idx) {
    if (a[idx] > a[idx + 1]) {
      break;
    }
  }
  if (idx == N - 1) {
    printf("Case #%d: %s\n",test_id, a);
    return;
  }

  while (a[idx] == '0' || (idx > 0 && a[idx] - 1 < a[idx - 1])) --idx;
  a[idx] -= 1;
  ++idx;
  for (;idx < N; ++idx) {
    a[idx] = '9';
  }
  while(*a == '0') ++a;
  printf("Case #%d: %s\n",test_id, a);
}

int main() {
  int tests;
  scanf("%d", &tests);

  for (int i = 1; i <= tests; ++i) {
    solve(i);
  }
}
