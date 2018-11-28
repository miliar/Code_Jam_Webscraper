#include<bits/stdc++.h>
#define In freopen("E:\\GitHub\\acm\\gcj\\2017\\A-large.in", "r", stdin);
#define Out freopen("E:\\GitHub\\acm\\gcj\\2017\\solve_out.txt", "w", stdout);

const int maxn = 1100;

using namespace std;


int main() {
  In
  Out
  int T;
  for (int t = scanf("%d", &T); t <= T; t++) {
    int K;
    char rows[maxn];
    scanf("%s%d", rows, &K);
    int S = strlen(rows);
    int ans = 0;
    bool isPossible = false;

    for (int endPos = S - 1; endPos >= 0; endPos--) {
      if (rows[endPos] == '+') {
        continue;
      }

      if (endPos + 1 < K) {
        isPossible = true;
        break;
      }

      ans++;
      for (int index = 0; index < K; index++) {
        rows[endPos - index] = rows[endPos - index] == '+' ? '-' : '+';
      }
    }
    printf("Case #%d: ", t);
    if (isPossible == false) {
      printf("%d\n", ans);
    } else {
      puts("IMPOSSIBLE");
    }
  }
  return 0;
}
