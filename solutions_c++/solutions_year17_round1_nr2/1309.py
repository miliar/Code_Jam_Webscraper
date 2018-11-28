#include <iostream>
#include <vector>
#include <set>
#include <cmath>
using namespace std;

class comparisonObj {
public:
    bool operator()(const pair<int, int> &p1, const pair<int, int> &p2) const{
        if (p1.first < p2.first)
            return true;
        if (p2.first < p1.first)
            return false;
        return p1.second < p2.second;
    }
};

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N, P;
        cin >> N >> P;
        double R[N][2], temp;
        for (int j = 0; j < N; ++j) {
            cin >> temp;
            R[j][0] = temp * 0.9;
            R[j][1] = temp * 1.1;
        }
        vector<multiset<pair<int, int>, comparisonObj>> Q{N};
        double t;
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < P; ++k) {
                cin >> t;
                if (ceil(t / R[j][1]) <= floor(t / R[j][0]))
                    Q[j].emplace(ceil(t / R[j][1]), floor(t / R[j][0]));
            }
        }

        int servings = 1;
        int num_kits = 0;
        bool done = false;
        while (!done) {
            char recipe[N]{};
            for (int j = 0; j < N; ++j) {
                if (Q[j].size() && servings < Q[j].begin()->first) {
                    servings = Q[j].begin()->first;
                    break;
                }
                while (Q[j].size() && servings > Q[j].begin()->second)
                    Q[j].erase(Q[j].begin());
                if (!Q[j].size()) {
                    done = true;
                    break;
                }
                else {
                    recipe[j] = 1;
                }
            }
            if (recipe[N - 1]) {
                for (int j = 0; j < N; ++j)
                    Q[j].erase(Q[j].begin());
                ++num_kits;
            }
        }
        cout << "Case #" << i + 1 << ": " << num_kits << endl;
    }
    return 0;
}
