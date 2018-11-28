#include <iostream>
using namespace std;

int dp[2][2][2][721]; //parity, who started at 0, who has right now, how long did C have --> min change
int a[1440];

int T;

int main() {
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int ac, aj;
        cin >> ac >> aj;
        for (int t = 0; t < 1440; t++) a[t] = -1;
        for (int i = 0; i < ac; i++) {
            int c, d;
            cin >> c >> d;
            for (int t = c; t < d; t++) a[t] = 0;
        }
        for (int i = 0; i < aj; i++) {
            int j, k;
            cin >> j >> k;
            for (int t = j; t < k; t++) a[t] = 1;
        }

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int h = 0; h <= 720; h++) {
                    dp[0][i][j][h] = 2000;
                }
            }
        }
        if (a[0] != 0) dp[0][0][0][1] = 0;
        if (a[0] != 1) dp[0][1][1][0] = 0;
        for (int t = 1; t < 1440; t++) {
            int o = (t+1)%2, n = t%2;
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 2; j++) {
                    for (int h = 0; h <= 720; h++) {
                        dp[n][i][j][h] = 2000;
                    }
                }
            }
            for (int started = 0; started < 2; started++) {
                for (int has = 0; has < 2; has++) {
                    for (int time_had = 0; time_had <= 720; time_had++) {
                        if (a[t] != 0 && time_had < 720) {
                            dp[n][started][0][time_had + 1] = min(dp[n][started][0][time_had + 1],
                                                                 dp[o][started][has][time_had] + (has == 0 ? 0 : 1));
                        }
                        if(a[t] != 1) {
                            dp[n][started][1][time_had] = min(dp[n][started][1][time_had],
                                                             dp[o][started][has][time_had] + (has == 1 ? 0 : 1));
                        }
                    }
                }
            }
        }
        cout << "Case #" << test << ": " << min(min(min(dp[1][0][0][720], dp[1][0][1][720]+1), dp[1][1][0][720]+1), dp[1][1][1][720]) << endl;
    }
    return 0;
}
