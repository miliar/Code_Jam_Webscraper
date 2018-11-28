#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>

using namespace std;

int bucket[4];

int main() {
  int t, n, p;

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    scanf("%d %d", &n, &p);
    for (int i = 0; i < 4; i++) {
      bucket[i] = 0;
    }
    for (int i = 0; i < n; i++) {
      int a;
      scanf("%d", &a);
      bucket[a % p] += 1;
    }
    int ans = 0;
    ans += bucket[0];
    if (p == 2) {
      ans += bucket[1] / 2;
      bucket[1] %= 2;
    } else if (p == 3) {
      int x = min(bucket[1], bucket[2]);
      ans += x;
      bucket[1] -= x;
      bucket[2] -= x;
      ans += bucket[1] / 3 + bucket[2] / 3;
      bucket[1] %= 3;
      bucket[2] %= 3;
    }/* else if (p == 4) {
      int x = min(bucket[1], bucket[3]);
      ans += x;
      bucket[1] -= x;
      bucket[3] -= x;
    }*/
    if (bucket[1] || bucket[2] || bucket[3]) {
      ans += 1;
    }
    printf("Case #%d: %d\n", o + 1, ans);
  }

  return 0;
}
