#include "stdafx.h"
#include "R1A_B.h"

pair<int, int> FindLimits(int val, int fact) {
    int min = 10 * val / fact / 11;
    if (11 * min * fact < 10 * val)
        min++;
    int max = 10 * val / fact / 9;
    if (9 * max * fact > 10 * val)
        max--;
    return make_pair(min, max);
}

void R1A_B::Solve() {
    int n, p, t;
    cin >> n >> p;
    vector<int> v;
    vector<int> iter;
    for (int i = 0; i < n; ++i) {
        cin >> t;
        v.push_back(t);
        iter.push_back(0);
    }
    vector<pair<int, int>> q[100];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            cin >> t;
            auto w = FindLimits(t, v[i]);
            if (w.first <= w.second)
                q[i].push_back(w);
        }
        sort(q[i].begin(), q[i].end());
    }
    
    int min, max, ans = 0;
    for (int i = 0; i < q[0].size(); ++i){
        min = q[0][i].first;
        max = q[0][i].second;
        bool good = true;
        for (int j = 1; j < n; ++j) {
            if (iter[j] >= q[j].size()) {
                good = false;
                break;
            }
            while (iter[j] < q[j].size() && q[j][iter[j]].second < min) {
                ++iter[j];
            }
            if (iter[j] == q[j].size() || q[j][iter[j]].first > max) {
                good = false;
                break;
            }
        }
        if (good) {
            ++ans;
            for (int j = 1; j < n; ++j)
                ++iter[j];
        }
    }
    cout << ans << endl;
}
