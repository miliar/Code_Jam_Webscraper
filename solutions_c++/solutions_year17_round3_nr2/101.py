#include <bits/stdc++.h>
using namespace std;

#define CAMERON 0
#define JAMIE 1
#define INF 0x33433433

int T;
int AC;
int AJ;
int dp[1500][1500][2]; //jamie
int sche[1500];

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    fill(sche, sche+1500, -1);

    scanf("%d%d", &AC, &AJ);
    for (int i=0; i<AC; i++) {
      int C, D;
      scanf("%d%d", &C, &D);
      for (int j=C; j<D; j++) {
        sche[j] = JAMIE;
      }
    }

    for (int i=0; i<AJ; i++) {
      int C, D;
      scanf("%d%d", &C, &D);
      for (int j=C; j<D; j++) {
        sche[j] = CAMERON;
      }
    }

    fill(dp[0][0], dp[1450][0], INF);
    
    int ans = INF;
    if (sche[0] != CAMERON) {
      dp[1][1][JAMIE] = 0;
      for (int i=1; i<1440; i++) {
        for (int j=0; j<=i; j++) {
          for (int k=0; k<=1; k++) {
            if (sche[i] != CAMERON) {
              int t = dp[i][j][k];
              if (k != JAMIE) t++;
              dp[i+1][j+1][JAMIE] = min(dp[i+1][j+1][JAMIE], t);
            }

            if (sche[i] != JAMIE) {
              int t = dp[i][j][k];
              if (k != CAMERON) t++;
              dp[i+1][j][CAMERON] = min(dp[i+1][j][CAMERON], t);
            }
          }
        }
      }

      //printf("dp[1440][720][JAMIE]:%d dp[1440][720][CAMERON]:%d\n", dp[1440][720][JAMIE], dp[1440][720][CAMERON]);
      ans = min(ans, min(dp[1440][720][JAMIE], dp[1440][720][CAMERON]+1));
    }

    fill(dp[0][0], dp[1450][0], INF);

    if (sche[0] != JAMIE) {
      dp[1][0][CAMERON] = 0;
      for (int i=1; i<1440; i++) {
        for (int j=0; j<=i; j++) {
          for (int k=0; k<=1; k++) {
            if (sche[i] != CAMERON) {
              int t = dp[i][j][k];
              if (k != JAMIE) t++;
              dp[i+1][j+1][JAMIE] = min(dp[i+1][j+1][JAMIE], t);
            }

            if (sche[i] != JAMIE) {
              int t = dp[i][j][k];
              if (k != CAMERON) t++;
              dp[i+1][j][CAMERON] = min(dp[i+1][j][CAMERON], t);
            }
          }
        }
      }

      //printf("dp[1440][720][JAMIE]:%d dp[1440][720][CAMERON]:%d\n", dp[1440][720][JAMIE], dp[1440][720][CAMERON]);
      ans = min(ans, min(dp[1440][720][CAMERON], dp[1440][720][JAMIE]+1));
    }

    printf("Case #%d: %d\n", Case, ans);
  }
}
