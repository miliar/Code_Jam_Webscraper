#include <bits/stdc++.h>
using namespace std;

int ac, aj;
bool empt[1500][2];
int dp[1500][1500][2];

int main() {
  int kase;
  scanf("%d", &kase);
  for(int ka = 0; ka < kase; ka++) {
    scanf("%d%d", &ac, &aj);
    memset(empt, 0, sizeof(empt));
    for(int i = 0; i < ac; i++) {
      int x, y;
      scanf("%d%d", &x, &y);
      for(int i = x+1; i <= y; i++) {
        empt[i][0] = 1;
      }
    }
    for(int i = 0; i < aj; i++) {
      int x, y;
      scanf("%d%d", &x, &y);
      for(int i = x+1; i <= y; i++) {
        empt[i][1] = 1;
      }
    }
    memset(dp, 127, sizeof(dp));
    dp[0][0][0] = 0;
    for(int i = 1; i <= 1440; i++) {
      for(int j = 0; j <= min(i, 720); j++) {
        for(int k = 0; k <= 1; k++) {
          if(empt[i][k]) continue;
          if(j == 0) {
            if(k != 1) continue;
            dp[i][j][k] = dp[i - 1][j][1];
          } else if (i==j) {
            if(k != 0) continue;
            dp[i][j][k] = dp[i - 1][j-1][0];
          } else {
            dp[i][j][k] = min(dp[i - 1][j - (k == 0) ][k],
            dp[i - 1][j - (k == 0)][k ^ 1] + 1);
          }
        }
      }
    }
// 、    cout<<dp[1440][720][0]<<endl;return 0;
      int p=min(dp[1440][720][0], dp[1440][720][1]+1);

    memset(dp, 127, sizeof(dp));
    dp[0][0][1] = 0;
    for(int i = 1; i <= 1440; i++) {
      for(int j = 0; j <= min(i, 720); j++) {
        for(int k = 0; k <= 1; k++) {
          if(empt[i][k]) continue;
          if(j == 0) {
            if(k != 1) continue;
            dp[i][j][k] = dp[i - 1][j][1];
          } else if (i==j) {
            if(k != 0) continue;
            dp[i][j][k] = dp[i - 1][j-1][0];
          } else {
            dp[i][j][k] = min(dp[i - 1][j - (k == 0) ][k],
            dp[i - 1][j - (k == 0)][k ^ 1] + 1);
          }
        }
      }
    }

    int p2=min(dp[1440][720][0]+1, dp[1440][720][1]);


    printf("Case #%d: ", ka + 1);
    printf("%d\n", min(p,p2));
  }
  return 0;
}
