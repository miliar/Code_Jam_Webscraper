#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#define For(i, n) for(int i = 0; i < (n); i ++)
using namespace std;
const int DAY = 24 * 60;
int dp[DAY][DAY/2 + 1][2][2], day[DAY], Inf = DAY + 10;
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int tc = 1; tc <= t; tc ++) {
        For(i, DAY) day[i] = 0;
        int ac, aj;
        cin >> ac >> aj;
        For(i, ac) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; j ++)
                day[j] = 1;
        }
        For(i, aj) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; j ++)
                day[j] = 2;
        }
        For(i, DAY) For(q, DAY/2 + 1) For(cl, 2) For(last, 2) {
            int &X = dp[i][q][cl][last];
            X = Inf;
            if (q - cl < 0) continue;
            if (cl+1 == day[i]) continue;
            if (!i) dp[0][cl][cl][last] = (last != cl);
            else {
                X = dp[i - 1][q - cl][cl][last];
                X = min(X, dp[i - 1][q - cl][!cl][last] + 1);
            }
            if (i == DAY - 1 && cl != last) X = Inf;
        }
        cout << "Case #" << tc << ": ";
        cout << min(dp[DAY - 1][DAY / 2][0][0], dp[DAY - 1][DAY / 2][1][1]) << endl;
    }
    return 0;
}
