#include <iostream>
#include <map>
#include <vector>
#include <queue>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    auto started = std::chrono::high_resolution_clock::now();

    int tc;
    cin >> tc;

    for (int tc_i = 0; tc_i < tc; tc_i++) {
        int d, n;
        cin >> d >> n;

        pair<int, int> horse[1001];

        for (int i = 0; i < n; i++) {
            cin >> horse[i].first >> horse[i].second;
        }

        sort(horse, horse + n);

        double l = .0, r = 1000000000000.0;

        while (((r - l) / r) > .000000001) {
            double mid = l + (r - l) / 2;
            double dis = 1.0 * d;

            for (int i = n - 1; i >= 0; i--) {
                dis = min(dis, 1.0 * horse[i].first + (mid * horse[i].second));
            }

            if (dis < d) {
                l = mid;
            }
            else {
                r = mid;
            }
        }

        cout << "Case #" << (tc_i + 1) << ": ";
        printf("%.7f", (1.0 * d / l));
//        cout << l;
        cout << endl;
    }

//    auto done = std::chrono::high_resolution_clock::now();
//    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(done-started).count();

    return 0;
}