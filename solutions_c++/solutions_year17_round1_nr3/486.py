#include <iostream>
#include <cmath>
#include <queue>

using namespace std;

const int N = 105;
const int INF = 1 << 20;
int dp[N][N][N][N];

int main() {
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    int H1, A1, H2, A2, B, D;
    cin >> H1 >> A1 >> H2 >> A2 >> B >> D;

    memset(dp, 63, sizeof(dp));
    dp[H1][A1][H2][A2] = 0;

    queue<int> qh1, qh2, qa1, qa2;
    qh1.push(H1);
    qa1.push(A1);
    qh2.push(H2);
    qa2.push(A2);

    int ret = INF;

    while (!qh1.empty()) {
      int h1 = qh1.front(); qh1.pop();
      int a1 = qa1.front(); qa1.pop();
      int h2 = qh2.front(); qh2.pop();
      int a2 = qa2.front(); qa2.pop();

      int &d = dp[h1][a1][h2][a2];
      if (h1 == 0) {
        continue;
      }
      if (h2 == 0) {
        ret = d;
        break;
      }

      // attack
      {
        int nh2 = max(h2 - a1, 0);
        int nh1;
        if (nh2 > 0) {
          nh1 = max(h1 - a2, 0);
        } else {
          nh1 = h1;
        }
        int &nd = dp[nh1][a1][nh2][a2];
        if (d + 1 < nd) {
          nd = d + 1;
          qh1.push(nh1);
          qa1.push(a1);
          qh2.push(nh2);
          qa2.push(a2);
        }
      }

      // buff
      {
        int nh1 = max(h1 - a2, 0);
        int na1 = min(a1 + B, H2);
        int &nd = dp[nh1][na1][h2][a2];
        if (d + 1 < nd) {
          nd = d + 1;
          qh1.push(nh1);
          qa1.push(na1);
          qh2.push(h2);
          qa2.push(a2);
        }
      }

      // cure
      {
        int nh1 = max(H1 - a2, 0);
        int &nd = dp[nh1][a1][h2][a2];
        if (d + 1 < nd) {
          nd = d + 1;
          qh1.push(nh1);
          qa1.push(a1);
          qh2.push(h2);
          qa2.push(a2);
        }
      }

      // debuff
      {
        int na2 = max(a2 - D, 0);
        int nh1 = max(h1 - na2, 0);
        int &nd = dp[nh1][a1][h2][na2];
        if (d + 1 < nd) {
          nd = d + 1;
          qh1.push(nh1);
          qa1.push(a1);
          qh2.push(h2);
          qa2.push(na2);
        }
      }
    }

    printf("Case #%d: ", t + 1);
    if (ret >= INF) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ret);
    }
  }
}
