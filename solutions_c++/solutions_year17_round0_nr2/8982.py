#include <iostream>
#include <cstdio>

using namespace std;

bool is_tidy(int x) {
  int y = 10;
  while (x > 0) {
    int z = x % 10;
    if (z > y) { 
      return false;
    } else {
      y = z;
    }
    x = x / 10;
  }
  return true;
}

int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int n;
    scanf("%d", &n);
    for (int i = n; i > 0; i--) {
      if (is_tidy(i)) {
        printf("%d\n", i);
        break;
      }
    }
  }
  return 0;
}