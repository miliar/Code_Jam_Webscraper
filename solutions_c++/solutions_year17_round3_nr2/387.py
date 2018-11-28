


#include<iostream>

using namespace std;

int dp[1500][730][2][2];
int flag[1500];
const int inf = 0x3f3f3f3f;
int Min(int &x, int y) {
    if (x > y) x = y;
}

int main() {
      freopen("../B-large.in","r",stdin);
      freopen("../B-large.out","w",stdout);
    int cas = 1;
    int T;
    cin >> T;
    while (T--) {
        printf("Case #%d: ",cas++);
        int n, m;
        cin >> n >> m;
        memset(flag, -1, sizeof(flag));
        for (int i = 1; i <= n; i++) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; ++j) {
                flag[j] = 0;
            }
        }
        for (int i = 1; i <= m; i++) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; ++j) {
                flag[j] = 1;
            }
        }
        for (int i = 0; i < 1440; i++)
            for (int j = 0; j <= 720; j++) {
                for (int k = 0; k <= 1; k++) {
                    for (int f = 0; f <= 1; f++) {
                        dp[i][j][k][f] = inf;
                    }
                }
            }
        if (flag[0] != -1) {
            if (flag[0] == 0) { //初始位置只能是1
                dp[0][0][1][1] = 0;
            } else if (flag[0] == 1) {//初始位置只能是0
                dp[0][1][0][0] = 0;
            }
        } else {
            dp[0][1][0][0] = 0;
            dp[0][0][1][1] = 0;
        }
        for (int i = 0; i < 1440; i++) {
            int next = (i + 1);
            for (int j = 0; j <= 720; j++) {
                for (int k = 0; k <= 1; k++) {
                    for (int f = 0; f <= 1; f++)
                        if (dp[i][j][k][f] != inf) {
                            //if(i == 1339){
                             //   cout<<j<<" "<<k<<" "<<f<<" "<<dp[i][j][k][f]<<endl;
                            //}
                            if (flag[next] == 0) { //必定1做
                                Min(dp[next][j][1][f], dp[i][j][k][f] + (k != 1));
                            } else if (flag[next] == 1) {
                                Min(dp[next][j + 1][0][f], dp[i][j][k][f] + (k != 0));
                            } else if (flag[next] == -1) {
                                Min(dp[next][j][1][f], dp[i][j][k][f] + (k != 1));
                                Min(dp[next][j + 1][0][f], dp[i][j][k][f] + (k != 0));
                            }
                        }
                }
            }
        }
        int ans = inf;
        Min(ans, dp[1439][720][0][0]);
        Min(ans, dp[1439][720][0][1] + 1);
        Min(ans, dp[1439][720][1][0] + 1);
        Min(ans, dp[1439][720][1][1] );
        cout << ans << endl;

    }


}
//3 1 4 1
/*
 *
 11
10
1 2 7 10 3 4 5 6 8 9
1 6 9 8 2 7 10 3 5 4
 */