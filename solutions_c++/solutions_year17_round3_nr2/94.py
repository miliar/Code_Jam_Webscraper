#include <bits/stdc++.h>
using namespace std;

struct Activity {
    int C, D;
};

int dp[2][2][721][721];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int AC, AJ;
        cin >> AC >> AJ;
        
        vector<Activity> Cameron(AC), Jamie(AJ);
        for (int i = 0; i < AC; i++) {
            cin >> Cameron[i].C >> Cameron[i].D;
        }
        for (int i = 0; i < AJ; i++) {
            cin >> Jamie[i].C >> Jamie[i].D;
        }

        vector<int> busy(1440, -1);
        for (auto a : Cameron) {
            for (int d = 0; d < a.D - a.C; d++)
                busy[a.C + d] = 0;
        }
        for (auto a : Jamie) {
            for (int d = 0; d < a.D - a.C; d++)
                busy[a.C + d] = 1;
        }

        // for (int i = 0; i < 1440; i++) {
        //     cout << i << ": " << busy[i] << endl;
        // }
        
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                for (int m = 0; m <= 720; m++)
                    for (int n = 0; n <= 720; n++)
                        dp[i][j][m][n] = 9999999;

        if (busy[0] != 0)
            dp[0][0][1][0] = 0;
        if (busy[0] != 1)
            dp[1][1][0][1] = 0;

        for (int time = 2; time <= 1440; time++) {
            for (int cam = 0; cam <= 720; cam++) {
                int jam = time - cam;
                if (!(cam <= time && jam >= 0 && jam <= time && jam <= 720)) continue;

                for (int start = 0; start < 2; start++) {
                    // cameran takes it
                    if (cam > 0 && busy[time-1] != 0) {
                        dp[start][0][cam][jam] = min(dp[start][0][cam][jam], dp[start][0][cam-1][jam]);
                        dp[start][0][cam][jam] = min(dp[start][0][cam][jam], dp[start][1][cam-1][jam] + 1);
                    }

                    // jamie takes it
                    if (jam > 0 && busy[time-1] != 1) {
                        dp[start][1][cam][jam] = min(dp[start][1][cam][jam], dp[start][1][cam][jam-1]);
                        dp[start][1][cam][jam] = min(dp[start][1][cam][jam], dp[start][0][cam][jam-1] + 1);
                    }
                }
            }
        }

        int best = numeric_limits<int>::max();
        best = min(best, dp[0][0][720][720]);
        best = min(best, dp[1][1][720][720]);
        best = min(best, dp[0][1][720][720] + 1);
        best = min(best, dp[1][0][720][720] + 1);

        cout << "Case #" << t << ": " << best;
        cout << '\n';
    }
    
}
