#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    freopen("/home/nimloth/coding/6sem/codejam/B-large (4).in", "r", stdin);
    freopen("output.txt", "w", stdout);
//    cout.setf(ios::fixed);
//    cout.precision(13);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int ans = 0;
        int c[105], d[105];
        int j[105], k[105];
        int ac, aj;
        pair<pair<int, int>, int> activities[205];
        pair<int, int> gaps[205];
        cin >> ac >> aj;
        int timec = 0;
        int timej = 0;
        for (int i = 0; i < ac; i++) {
            cin >> c[i] >> d[i];
            timej += d[i] - c[i];
            activities[i] = make_pair(make_pair(c[i], d[i]), 0);
        }
        for (int i = 0; i < aj; i++) {
            cin >> j[i] >> k[i];
            timec += k[i] - j[i];
            activities[ac + i] = make_pair(make_pair(j[i], k[i]), 1);
        }
        sort(activities, activities + ac + aj);
        pair<pair<int, int>, int> prev = activities[0];
        int z = 0;
        for (int i = 1; i < ac + aj; i++) {
            if (prev.second == activities[i].second) {
                gaps[z] = make_pair(activities[i].first.first - prev.first.second, prev.second);
                z++;
            } else {
                ans++;
            }
            prev = activities[i];
        }
        if (activities[0].second == activities[ac + aj - 1].second) {
            gaps[z] = make_pair(activities[0].first.first + 24 * 60 - activities[ac + aj - 1].first.second, activities[0].second);
            z++;
        } else {
            ans++;
        }

        sort(gaps, gaps + z);

        for (int i = 0; i < z; i++) {
            if (gaps[i].second == 0) {
                if (timej + gaps[i].first <= 720) {
                    timej += gaps[i].first;
                } else {
                    ans += 2;
                }
            } else {
                if (timec + gaps[i].first <= 720) {
                    timec += gaps[i].first;
                } else {
                    ans += 2;
                }
            }
        }

        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}