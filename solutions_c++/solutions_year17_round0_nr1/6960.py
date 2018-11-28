#include <bits/stdc++.h>

using namespace std;

int solve(string const &pancakes, int range) {
    vector<int> t(pancakes.size(), 0);
    for (int i = 0; i < t.size(); ++i) {
        const int prev_1 = (i-1<0 ? 0 : t[i-1]);
        const int prev_range = (i-range<0 ? 0 : t[i-range]);
        const int flips_num = prev_1 - prev_range;
        assert(flips_num >= 0);
        if (pancakes[i] == '+') {
            t[i] += prev_1 + (flips_num % 2 == 1 ? 1 : 0);
        } else {
            t[i] += prev_1 + (flips_num % 2 == 0 ? 1 : 0);
        }
    }

    if (0) {
        for (int k : t) {
            cout << k << " ";
        }
        cout << endl;
    }

    const int lastFlip = t[t.size()-range];
    if (lastFlip != t[t.size()-1]) {
        return -1;
    }

    return lastFlip;
}

int main() {
    int case_num;
    cin >> case_num;

    for (int i = 0; i < case_num; ++i) {
        string pancakes;
        cin >> pancakes;
        int range;
        cin >> range;
        // cout << pancakes << " " << range << endl;
        int ans = solve(pancakes, range);
        if (ans == -1) {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << solve(pancakes, range) << endl;
        }
    }

    return 0;
}
