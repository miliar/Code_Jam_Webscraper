#include <iostream>
#include <algorithm>
#include <utility>
#include <iomanip>

using namespace std;

bool cross(pair<int, int>, pair<int, int>, int d);

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i_t = 0; i_t < t; i_t++) {
        int d, n;
        pair<int, int> k[1002];
        cin >> d >> n;
        for (int i = 0; i < n; i++) {
            cin >> k[i].first >> k[i].second;
        }
        sort(k, k + n);
        for (int i = 0; i < n; i++) {
            bool flag = false;
            for (int j = i + 1; j < n; j++) {
                if (cross(k[i], k[j], d)) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                double res;
                res = d / ((d - k[i].first) * 1.0 / k[i].second);
                std::cout << std::fixed;
                cout << setprecision(6) << "Case #" << i_t + 1 << ": " << res << "\n";
                break;
            }
        }
    }
    return 0;
}

bool cross(pair<int, int> a, pair<int, int> b, int d) {
    if (a.second <= b.second) {
        return false;
    }
    return ((b.first - a.first) * 1.0 / (a.second - b.second) * b.second + b.first < d);
}
