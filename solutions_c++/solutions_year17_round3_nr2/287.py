#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int AC, AJ;
        cin >> AC >> AJ;
        vector<int> act(1440, -1);
        for (int ac = 0; ac < AC; ac++) {
            int CI, DI;
            cin >> CI >> DI;
            for (int c = CI; c < DI; c++) {
                act[c] = 0;
            }
        }
        for (int aj = 0; aj < AJ; aj++) {
            int JI, KI;
            cin >> JI >> KI;
            for (int j = JI; j < KI; j++) {
                act[j] = 1;
            }
        }
        int dp[721][721][2][2];
        for (int i = 0; i < 721; i++) {
            for (int j = 0; j < 721; j++) {
                for (int m = 0; m < 2; m++) {
                    for (int n = 0; n < 2; n++) {
                        dp[i][j][m][n] = 1000000;
                    }
                }
            }
        }
        if (act[0] != 0) {
            dp[1][0][0][0] = 0;
        }
        if (act[0] != 1) {
            dp[0][1][1][1] = 0;
        }
        for (int minute = 2; minute <= 1440; minute++) {
            for (int i = 0; i <= minute; i++) {
                int j = minute - i;
                if (i > 720 || j > 720) {
                    continue;
                }
                for (int m = 0; m < 2; m++) {
                    for (int c = 0; c < 2; c++) {
                        if (act[minute - 1] == c) {
                            continue;
                        }
                        int prevI = i;
                        int prevJ = j;
                        if (c == 0) {
                            prevI--;
                        } else {
                            prevJ--;
                        }
                        if (prevI < 0 || prevJ < 0) {
                            continue;
                        }
                        int res = 1000000;
                        for (int n = 0; n < 2; n++) {
                            if (c == n) {
                                res = min(res, dp[prevI][prevJ][m][n]);
                            } else {
                                res = min(res, dp[prevI][prevJ][m][n] + 1);
                            }
                        }
                        if (res != 1000000) {
                            dp[i][j][m][c] = res;
                        }
                    }
                }
            }
        }
        int res = 1000000;
        for (int m = 0; m < 2; m++) {
            for (int n = 0; n < 2; n++) {
                if (m == n) {
                    res = min(res, dp[720][720][m][n]);
                } else {
                    res = min(res, dp[720][720][m][n] + 1);
                }
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
