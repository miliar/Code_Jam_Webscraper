#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

const double PI = std::atan(1.0)*4;

int solve(int ai, int aj, vector<pair<int, int>> &a) {
    sort(a.begin(), a.end());
    if (ai == 0 || aj == 0) {
        if (ai == 1 || aj == 1) { // 1 - 0
            return 2;
        } else { // 2 - 0
            int l1 = a[0].second - a[0].first;
            int l2 = a[1].second - a[1].first;
            if (a[1].first - a[0].second + l1 + l2 <= 720 || l1 + l2 + a[0].first + 24 * 60 - a[1].second <= 720) return 2;
            return 4;
        }
    } else { // 1 - 1
        return 2;
    }
}

int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int ai, aj;
        cin >> ai >> aj;
        vector<pair<int, int>> a(ai + aj);
        for (int i = 0; i < ai + aj; ++i) {
            cin >> a[i].first >> a[i].second;
        }
        int res = solve(ai, aj, a);
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
