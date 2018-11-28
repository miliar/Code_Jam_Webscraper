#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

const double PI = 3.141592653589793238463;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        vector<pair<int, int>> pancakes(N);
        for (int n = 0; n < N; n++) {
            cin >> pancakes[n].first >> pancakes[n].second;
        }
        double ans = 0.0;
        for (int i = 0; i < N; i++) {
            vector<double> auxAreas;
            for (int j = 0; j < N; j++) {
                if (j == i) {
                    continue;
                }
                if (pancakes[i].first < pancakes[j].first) {
                    continue;
                }
                auxAreas.push_back(2.0 * PI * (double) pancakes[j].second * (double) pancakes[j].first);
            }
            if ((int)auxAreas.size() + 1 < K) {
                continue;
            }
            sort(auxAreas.begin(), auxAreas.end());
            reverse(auxAreas.begin(), auxAreas.end());
            double area = PI * (double) pancakes[i].first * (double) pancakes[i].first;
            area += 2.0 * PI * (double) pancakes[i].first * (double) pancakes[i].second;
            for (int k = 0; k + 1 < K; k++) {
                area += auxAreas[k];
            }
            if (area > ans) {
                ans = area;
            }
        }
        cout << "Case #" << t << ": " << fixed << setprecision(9) << ans << endl;
    }
    return 0;
}
