#include <bits/stdc++.h>

using namespace std;

#define INF 100000000
#define YJ 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long
#define LD long double

using namespace std;

int T;

#define MAX_A 105
#define MAX_T 1441

int Ac, Aj;
int C[MAX_A], D[MAX_A];
int J[MAX_A], K[MAX_A];

bool usedA[MAX_T], usedB[MAX_T];

void init()
{
  memset(usedA, 0, sizeof(usedA));
  memset(usedB, 0, sizeof(usedB));
}

void input()
{
  init();

  cin >> Ac >> Aj;
  for (int i = 0; i < Ac; i++) {
    cin >> C[i] >> D[i];
    for (int j = C[i]; j < D[i]; j++) {
      usedA[j] = true;
    }
    /*
    if(C[i] == 0){
      usedA[1440] = true;
    }
    */
  }
  for (int i = 0; i < Aj; i++) {
    cin >> J[i] >> K[i];
    for (int j = J[i]; j < K[i]; j++) {
      usedB[j] = true;
    }
    /*
    if(J[i] == 0){
      usedB[1440] = true;
    }
    */
  }
}

int dp[MAX_T][MAX_T][2][2];
int main()
{

  cin >> T;
  for (int testcase = 0; testcase < T; testcase++) {
    input();

    for (int i = 0; i < MAX_T; i++) {
      for (int j = 0; j < MAX_T; j++) {
        for (int k = 0; k < 2; k++) {
          for (int k2 = 0; k2 < 2; k2++) {
            dp[i][j][k][k2] = INF;
          }
        }
      }
    }

    if(!usedA[0]){
      dp[0][0][0][0] = 0;
    }
    if(!usedB[0]){
      dp[0][0][1][1] = 0;
    }

    for (int i = 0; i < 750; i++) {
      for (int j = 0; j < 750; j++) {
        for (int k = 0; k < 2; k++) {
          for (int k2 = 0; k2 < 2; k2++) {
            if(dp[i][j][k][k2] == INF){
              continue;
            }
            //そのまま
            if(k == 0 && !usedA[i+j]){
              dp[i+1][j][k][k2] = min(dp[i+1][j][k][k2], dp[i][j][k][k2]);
            }
            else if(k == 1 && !usedB[i+j]){
              dp[i][j+1][k][k2] = min(dp[i][j+1][k][k2], dp[i][j][k][k2]);
            }

            //相手に移す
            if(k == 0 && !usedB[i+j]){
              dp[i][j+1][(k+1)%2][k2] = min(dp[i][j+1][(k+1)%2][k2], dp[i][j][k][k2] + 1);
            }
            else if(k == 1 && !usedA[i+j]){
              dp[i+1][j][(k+1)%2][k2] = min(dp[i+1][j][(k+1)%2][k2], dp[i][j][k][k2] + 1);
            }
          }
        }
      }
    }

    int ans = min(min(dp[720][720][0][0], dp[720][720][1][1]), min(dp[720][720][0][0], dp[720][720][1][1]));

    ans = min(ans, min(min(dp[720][720][0][1], dp[720][720][1][0]), min(dp[720][720][0][1], dp[720][720][1][0])) + 1);

    printf("Case #%d: %d\n", testcase+1, ans);

  }

  return 0;
}
