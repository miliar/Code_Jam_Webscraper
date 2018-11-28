#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>


using namespace std;


struct horse {
    double speed, left, time;
    horse(double s, double l, double t): speed(s), left(l), time(t) {}
};


double solve() {
    int n, q;
    cin >> n >> q;
    vector<pair<double, double>> horses(n + 1, {0, 0});
    vector<vector<double>> dist(n + 1);
    vector<pair<int, int>> ways;

    for (int i = 0; i < n; i++) {
        cin >> horses[i].first >> horses[i].second;
    }

    for (int i = 0; i < n; i++) {
        dist[i].resize(n + 1);
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }

    for (int i = 0; i < q; i++) {
        int from, to;
        cin >> from >> to;
        ways.emplace_back(from, to);
    }


    int current = 0;
    list<horse> all;

    while (current < n) {
        double best_time = 0;
        if (current > 0) {
            best_time = all.front().time;
        }

        for (auto it = all.begin(); it != all.end(); ++it) {
            best_time = min(best_time, it -> time);
        }
        all.emplace_back(horses[current].second, horses[current].first, best_time);
        double next_dist = dist[current][current + 1];

        for (auto it = all.begin(); it != all.end();) {
            it -> left -= next_dist;
            if (it -> left < 0) {
                it = all.erase(it);
            } else {
                it -> time += next_dist / it -> speed;
                ++it;
            }
        }
        current++;
    }

    double best_time = all.front().time;

    for (auto it = all.begin(); it != all.end(); ++it) {
        best_time = min(best_time, it -> time);
    }

    return best_time;
}


int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output", "w", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        printf("Case #%d: %.7f\n", t + 1, solve());
    }

    return 0;
}
