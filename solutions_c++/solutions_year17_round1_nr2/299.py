#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int x[55][55], y[55];
vector<int> X[55][1000010];

int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        int N, P;
        cin >> N >> P;
        for (int i = 0; i < N; ++i) {
            cin >> y[i];
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j <= 1000000; ++j) X[i][j].clear();
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < P; ++j) {
                cin >> x[i][j];
                int K = round(1.0 * x[i][j] / y[i]);
                while (K * y[i] * 0.9 <= x[i][j] && x[i][j] <= 1.1 * K * y[i]) --K;
                ++K;

                if (K * y[i] * 0.9 <= x[i][j] && x[i][j] <= 1.1 * K * y[i]) {
                    X[i][K].push_back(x[i][j]);
                }
            }
        }

        int ans = 0;
        for (int i = 1; i <= 1000000; ++i) {
            int temp = P;
            for (int j = 0; j < N; ++j) temp = min(temp, (int)X[j][i].size());
            ans += temp;
            for (int j = 0; j < N; ++j) {
                sort(X[j][i].begin(), X[j][i].end());
                for (int l = temp; l < X[j][i].size(); ++l) {
                    if ((i + 1) * y[j] * 0.9 <= X[j][i][l] && X[j][i][l] <= (i + 1) * y[j] * 1.1) {
                        X[j][i + 1].push_back(X[j][i][l]);
                    }
                }
            }
        }
        cout << "Case #" << times << ": " << ans << endl;
    }

    return 0;
}