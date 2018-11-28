#include <iostream>
#include <algorithm>
using namespace std;

int myfixed[1440];

int dp[2][721][1441][2];

int solve() {
    int i, j, beg, end;
    
    // 'C' .. 0, 'J' .. 1
    
    // for (i=0; i<1440; i++) printf("%3d", myfixed[i]);
    
    for (i=0; i<=1440; i++) {
    for (j=0; j<=720; j++) {
        dp[0][j][i][0] = 100000;
        dp[0][j][i][1] = 100000;
        dp[1][j][i][0] = 100000;
        dp[1][j][i][1] = 100000;
    }
    }
    
    dp[0][0][0][0] = 0;
    dp[1][0][0][0] = 0;
    dp[0][0][0][1] = 0;
    dp[1][0][0][1] = 0;
    
    for (i=1; i<=1440; i++) {
        for (j=0; j<=720; j++) {
        for (beg=0; beg<=1; beg++) {
        for (end=0; end<=1; end++) {

            int o_end = 1 - end;
            int o_beg = 1 - beg;
            
            if (j > i || ((i == 1) && (beg != end))) {
                dp[beg][j][i][end] = 100000;
                continue;
            }
            
            // main
            int ans = 100000;
            int dd;
            
            if (myfixed[i - 1] != o_end && (j - ((end == 1)?1:0) >= 0)) {
                dd = dp[beg][j - ((end == 1)?1:0)][i - 1][end];
                ans = min(ans, dd);
            }
            
            if (myfixed[i - 1] != o_end && (j - ((end == 1)?1:0) >= 0)) {
                dd = dp[beg][j - ((end == 1)?1:0)][i - 1][o_end] + 1;
                ans = min(ans, dd);
            }
            
            dp[beg][j][i][end] = ans;
            
            // main
        } } }
    
    
    }

    int a = dp[0][720][1440][0];
    int b = dp[1][720][1440][0] + 1;
    int c = dp[0][720][1440][1] + 1;
    int d = dp[1][720][1440][1];
    // cout << a << " " << b << " " << c << " " << d << endl;
    return min(min(a, b), min(c, d));
}

int main() {
    int nCases;
    cin >> nCases;
    
    for (int i=1; i<=nCases; i++) {
        int ac, aj;
        cin >> ac >> aj;
        for (int j=0; j<=1440; j++) myfixed[j] = -1;
        int beg, end;
        for (int j=1; j<=ac; j++) {
            cin >> beg >> end;
            for (int k=beg; k < end; k++) myfixed[k] = 0;
        }
        for (int j=1; j<=aj; j++) {
            cin >> beg >> end;
            for (int k=beg; k < end; k++) myfixed[k] = 1;
        }
        int ans = solve();
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
