#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long double ld;

int d, n;
vector<pair<ld, ld>> h;

bool check(ld sp) {
    h[0].second = sp;

    vector<ld> coords(n + 1);
    vector<ld> speed(n + 1);
    for (int i = 0; i <= n; i++) {
        coords[i] = h[i].first;
        speed[i] = h[i].second;
    }
    vector<bool> used(n + 1);

    for (int i = 0; i < n; i++) {
        ld mn_col = INFINITY;
        int ind_col = -1;

        for (int j = 0; j < n; j++) {
            if (used[j]) continue;
            ld cur_col;
            if (speed[j + 1] >= speed[j]) {
                cur_col = INFINITY;
            } else {
                cur_col = (coords[j + 1] - coords[j]) / (speed[j] - speed[j + 1]);
                if (cur_col >= (d - coords[j + 1]) / speed[j + 1]) {
                    cur_col = INFINITY;
                }
            }

            if (cur_col <= mn_col) {
                mn_col = cur_col;
                ind_col = j;
            }
        }

        if (mn_col != INFINITY && ind_col == 0) {
            return false;
        } else if (mn_col == INFINITY) {
            return true;
        } else {
            used[ind_col] = true;
            speed[ind_col] = speed[ind_col + 1];

            for (int j = 0; j <= n; j++) {
                coords[j] += h[j].second * mn_col;
            }
        }
    }

    return true;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cin >> d >> n;
        h.resize(n + 1);
        for (int i = 1; i <= n; i++) {
            cin >> h[i].first >> h[i].second;
        }
        h[0].first = 0;
        sort(h.begin(), h.end());

        ld L = 0;
        ld R = 1000000000000000000;

        for (int i = 0; i < 100; i++) {
            ld M = (L + R) / 2;
            if (check(M)) {
                L = M;
            } else {
                R = M;
            }
        }

        cout.precision(20);
        cout << "Case #" << tt << ": " << L << endl;
    }

    return 0;
}