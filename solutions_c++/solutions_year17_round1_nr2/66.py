
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int solve() {
    int N, P;
    cin >> N >> P;
    vector <int> R(N);
    for (int i = 0; i < N; i++)
        cin >> R[i];

    vector <vector <pair <int, int>>> valid_all;
    for (int i = 0; i < N; i++) {
        vector <pair <int, int>> valid;
        for (int j = 0; j < P; j++) {
            int Q;
            cin >> Q;
            // 0.9*R*k <= Q <= 1.1*R*k
            // k >= Q/(1.1*R)
            // k <= Q/(0.9*R)
            int kmin = (10 * Q + (11 * R[i] - 1)) / (11 * R[i]);
            int kmax = (10 * Q) / (9 * R[i]);
            if (kmin > 0 && kmin <= kmax)
                valid.push_back({kmin, kmax});
        }
        sort(valid.begin(), valid.end());
        valid_all.push_back(valid);
    }

    int total = 0;
    while (true) {
        vector <int> vals;
        for (int i = 0; i < N; i++) {
            for (auto& p : valid_all[i]) {
                vals.push_back(p.first);
                vals.push_back(p.second);
            }
        }
        sort(vals.begin(), vals.end());

        bool found = false;
        for (int val : vals) {
            vector <int> idx;
            for (int i = 0; i < N; i++) {
                // use one with smallest right
                int best_idx = -1, best_right = 1e9;
                for (int j = 0; j < valid_all[i].size(); j++) {
                    auto p = valid_all[i][j];
                    if (val >= p.first && val <= p.second) {
                        if (p.second < best_right)
                            best_right = p.second, best_idx = j;
                    }
                }
                if (best_idx == -1)
                    break;
                idx.push_back(best_idx);
            }
            if (idx.size() == N) {
                for (int i = 0; i < N; i++)
                    valid_all[i].erase(valid_all[i].begin() + idx[i]);
                found = true;
                total++;
                break;
            }
        }
        if (!found)
            break;
    }
    return total;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
