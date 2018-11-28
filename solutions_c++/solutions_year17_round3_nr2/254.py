#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    int T;

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int n, m;
        cin >> n >> m;
        if (n + m == 0) {
            cout << "Case #" << t << ": 1\n";
            continue;
        }
        vector<tuple<int, int, int>> act(n + m);
        int has1 = 0, has2 = 0;
        for (int i = 0; i < n; ++i) {
            int x, y;
            cin >> x >> y;
            act[i] = make_tuple(x, y, 0);
            has2 += y - x;
        }
        for (int i = 0; i < m; ++i) {
            int x, y;
            cin >> x >> y;
            act[n + i] = make_tuple(x, y, 1);
            has1 += y - x;
        }
        sort(act.begin(), act.end());
        vector<int> d, e1, e2;
        int sum_d = 0, sum_e_1 = 0, sum_e_2 = 0;
        for (int i = 0; i < n + m; ++i) {
            int diff;
            if (i < n + m - 1) {
                diff = get<0>(act[i + 1]) - get<1>(act[i]);
            }
            else {
                diff = get<0>(act[0]) + 1440 - get<1>(act[i]);
            }
            int j = (i + 1) % (n + m);
            if (get<2>(act[i]) == get<2>(act[j])) {
                if (get<2>(act[i]) == 0) {
                    sum_e_2 += diff;
                    e2.push_back(diff);
                }
                else {
                    sum_e_1 += diff;
                    e1.push_back(diff);
                }
            }
            else {
                sum_d += diff;
                d.push_back(diff);
            }
        }
        sort(d.begin(), d.end());
        sort(e1.begin(), e1.end());
        sort(e2.begin(), e2.end());
        int sum1 = has1 + sum_e_1, sum2 = has2 + sum_e_2;
        if (sum1 > 720) {
            int counter = 0;
            int s = e1.size();
            for (int i = s - 1; i >= 0; --i) {
                counter += 2;
                int has_diff = sum1 - 720;
                if (has_diff <= e1[i]) {
                    break;
                }
                else {
                    sum1 -= e1[i];
                }
            }
            cout << "Case #" << t << ": " << d.size() + counter << "\n";
        }
        else if (sum2 > 720) {
            int counter = 0;
            int s = e2.size();
            for (int i = s - 1; i >= 0; --i) {
                counter += 2;
                int has_diff = sum2 - 720;
                if (has_diff <= e2[i]) {
                    break;
                }
                else {
                    sum2 -= e2[i];
                }
            }
            cout << "Case #" << t << ": " << d.size() + counter << "\n";
        }
        else {
            cout << "Case #" << t << ": " << d.size() << "\n";
        }
    }

    return 0;
}
