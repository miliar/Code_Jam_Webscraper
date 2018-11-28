#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, P;
        double U;
        cin >> N >> P;
        cin >> U;

        vector<double> cores;
        for (int i = 0; i < N; i++) {
            double x;
            cin >> x;
            cores.push_back(x);
        }

        sort(cores.begin(), cores.end());

        int i = 0;
        while (U > 0 && i < N - 1) {
            if (cores[i+1] > cores[i]) {
                double sum = 0;
                for (int k = 0; k <= i; k++) {
                    sum += cores[k];
                }
                double left = (i + 1) * cores[i+1] - sum;
                double to_use = min(left, U);
                U -= to_use;
                for (int k = 0; k <= i; k++)
                    cores[k] += to_use / (i + 1);
            }
            i++;
        }
        if (U > 0) {
            for (int i = 0; i < N; i++) {
                cores[i] += U / N;
            }
        }
        double ans = 1;
        for (int i = 0; i < N; i++)
            ans *= cores[i];
        printf("Case #%d: %.8lf\n", t, ans);
    }
    return 0;
}
