#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#define For(i, n) for(int i = 0; i < (n); i ++)
using namespace std;
const int M = 1e3 + 10;
double dp[M][M], pi = 3.141592653589793238462643;
vector <pair<int, int> > pan;
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int tc = 1; tc <= t; tc ++) {
        pan.clear();
        int n, k;
        cin >> n >> k;
        For(i, n) For(q, k + 1)
            dp[i][q] = 0;
        For(i, n) {
            int r, h;
            cin >> r >> h;
            pan.push_back(make_pair(r, h));
        }
        sort(pan.begin(), pan.end());
        reverse(pan.begin(), pan.end());
        For(i, n) {
            int r, h;
            r = pan[i].first;
            h = pan[i].second;
            if (!i)
                dp[0][1] = pi*r*r + 2*pi*r*h;
            else
                For(q, k + 1)
                    if (q == 1)
                        dp[i][1] = max(dp[i - 1][1], pi*r*r + 2*pi*r*h);
                    else
                        dp[i][q] = max(dp[i - 1][q], dp[i - 1][q - 1] + 2*pi*r*h);
        }
        cout << "Case #" << tc << ": ";
        cout << setprecision(10) << fixed << dp[n - 1][k] << endl;
    }
}
