#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>

using namespace std;

bool sortBySideArea(pair<int, pair<int, int>> a, pair<int, pair<int, int>> b) {
    return (1LL * a.first * a.second.first) < (1LL * b.first * b.second.first);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    auto started = std::chrono::high_resolution_clock::now();

    int tc;
    cin >> tc;

    pair<int, pair<int, int>> pan1[1010], pan2[1010];

    for (int tc_i = 0; tc_i < tc; tc_i++) {
        int n, k;

        cin >> n >> k;

        for (int i = 0; i < n; i++) {
            cin >> pan1[i].first >> pan1[i].second.first;
            pan1[i].second.second = i;
            pan2[i] = pan1[i];
        }

        sort(pan1, pan1 + n);
        sort(pan2, pan2 + n, sortBySideArea);

        long double res = .0;

        for (int i = n - 1; i >= 0; i--) {
            long double subRes = 1.0 * M_PI * pan1[i].first * pan1[i].first + 2 * M_PI * pan1[i].first * pan1[i].second.first;
            int k1 = k - 1;

            for (int j = n - 1; (j >= 0) && (k1 > 0); j--) {
                if (pan2[j].second.second == pan1[i].second.second) {
                    continue;
                }

                subRes += 2.0 * M_PI * pan2[j].first * pan2[j].second.first;
                k1--;
            }

            res = max(res, subRes);
        }

        cout << "Case #" << (tc_i + 1) << ": ";

        printf("%.10Lf", res);

        cout << endl;
    }

//    auto done = std::chrono::high_resolution_clock::now();
//    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(done-started).counter();

    return 0;
}