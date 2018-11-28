#include <iostream>
using namespace std;

int getbit(int n, int k) {
    return (n >> k) & 1;
}
void setbit(int &n, int k) {
    n ^= 1 << k;
}

int T;
int Ac, Aj;
int activity[1500];
int dp[1500][750][2][2];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    // freopen("input.txt", "r", stdin);

    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        memset(activity, 0, sizeof activity);

        cin >> Ac >> Aj;
        for (int i = 0; i < Ac; ++i) {
            int C, D;
            cin >> C >> D;
            setbit(activity[C], 0);
            setbit(activity[D], 0);
        }
        
        for (int i = 0; i < Aj; ++i) {
            int J, K;
            cin >> J >> K;
            setbit(activity[J], 1);
            setbit(activity[K], 1);
        }

        memset(dp, 63, sizeof dp);
        for (int i = 0, occupied = activity[0]; i < 24 * 60; occupied ^= activity[++i]) {
            if (i == 0) {
                if (!getbit(occupied, 0)) {
                    dp[i][1][0][0] = 1;
                }
                if (!getbit(occupied, 1)) {
                    dp[i][0][1][1] = 1;
                }
            } else {
                for (int j = 0; j <= i + 1; ++j) {
                    for (int k = 0; k < 2; ++k) {
                        if (!getbit(occupied, 0) && j > 0) {
                            dp[i][j][k][0] = min(dp[i - 1][j - 1][k][0], dp[i - 1][j - 1][k][1] + 1);
                        }
                        if (!getbit(occupied, 1)) {
                            dp[i][j][k][1] = min(dp[i - 1][j][k][1], dp[i - 1][j][k][0] + 1);
                        }
                    }
                }
            }
        }

        cout << "Case #" << tid + 1 << ": " << min(
            min(dp[24 * 60 - 1][720][0][0] - 1, dp[24 * 60 - 1][720][1][0]),
            min(dp[24 * 60 - 1][720][1][1] - 1, dp[24 * 60 - 1][720][0][1])) << endl;
    }

    return 0;
}