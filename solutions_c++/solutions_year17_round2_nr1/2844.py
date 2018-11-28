#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <limits>
#include <iomanip>
using namespace std;

float solve(int d, vector<pair<int, int>> &h) {
    // cout << d << endl;
    float max_h = std::numeric_limits<float>::min();
    int idx = 0;
    for (int i = 0; i < h.size(); ++i) {
        auto cur_t = (d-h[i].first)/float(h[i].second);
        //max_h = max(, max_h);
        if (cur_t > max_h) {
            idx = i;
            max_h = cur_t;
        }
    }

    return d/max_h;

}

int main() {
    int t;
    cin >> t;
    int i = 0;
    while (i++ < t) {
        int d, n;
        cin >> d >> n;
        int j = 0;
        vector<pair<int, int>> h;
        while (j++ < n) {
            int k, s;
            cin >> k >> s;
            h.emplace_back(k, s);
        }

        // cout << "Case #" << i << ": " << std::setprecision(6) << std::fixed << solve(d, h) << endl;
        printf("Case #%d: %.6f\n", i,  solve(d, h));
    }
}
