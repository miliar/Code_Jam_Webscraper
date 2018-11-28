#include <stdio.h>
#include <algorithm>

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int n, p;
    scanf("%d%d", &n, &p);
    int count[4];
    for(int i = 0; i < 4; i++)
      count[i] = 0;
    for(int i = 0; i < n; i++) {
      int val;
      scanf("%d", &val);
      count[val % p]++;
    }
    int answer = 0;
    if (p == 2) {
      int c;
      c = count[0];
      answer += c;
      count[0] -= c;

      c = count[1] / 2;
      answer += c;
      count[1] -= 2 * c;

      if (count[1] > 0)
        answer++;
    } else if (p == 3) {
      int c;
      c = count[0];
      answer += c;
      count[0] -= c;

      c = std::min(count[1], count[2]);
      answer += c;
      count[1] -= c;
      count[2] -= c;

      c = count[1] / 3;
      answer += c;
      count[1] -= 3 * c;

      c = count[2] / 3;
      answer += c;
      count[2] -= 3 * c;

      if (count[1] > 0 || count[2] > 0)
        answer++;
    } else if (p == 4) {
      int c;
      c = count[0];
      answer += c;
      count[0] -= c;

      c = std::min(count[1], count[3]);
      answer += c;
      count[1] -= c;
      count[3] -= c;

      c = count[2] / 2;
      answer += c;
      count[2] -= 2 * c;

      c = std::min(count[1] / 2, count[2]);
      answer += c;
      count[1] -= 2 * c;
      count[2] -= c;

      c = std::min(count[2], count[3] / 2);
      answer += c;
      count[2] -= c;
      count[3] -= 2 * c;

      c = count[3] / 4;
      answer += c;
      count[3] -= 4 * c;

      c = count[1] / 4;
      answer += c;
      count[1] -= 4 * c;

      if (count[1] > 0 || count[2] > 0 || count[3] > 0)
        answer++;
    }
    printf("Case #%d: %d\n", t, answer);
  }
  return 0;
}
