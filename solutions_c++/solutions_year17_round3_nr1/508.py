#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const double pi = 3.1415926535;

int main() {
    freopen("/home/nimloth/coding/6sem/codejam/A-large (4).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout.setf(ios::fixed);
    cout.precision(13);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int r[1005];
        int h[1005];
        pair<double, int> score[1005];
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
            score[i] = make_pair(2 * pi * double(r[i]) * double(h[i]), r[i]);
        }
        sort(score, score + n);
        reverse(score, score + n);
        double ans = 0;
        for (int i = 0; i < n; i++) {
            double cur_score = pi * score[i].second * score[i].second + score[i].first;
            int z = 1;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (score[j].second <= score[i].second && z < k) {
                        cur_score += score[j].first;
                        z++;
                    }
                }
                if (z == k) {
                    break;
                }
            }
            if (z == k) {
                ans = max(ans, cur_score);
            }
        }
        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}