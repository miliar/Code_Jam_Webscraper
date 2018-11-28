#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        int colors[3], zero;
        cin >> N;
        for (int i = 0; i < 3; i++) {
            cin >> colors[i] >> zero;
        }
        bool possible = true;
        for (int i = 0; i < 3; i++) {
            int i1 = (i + 1) % 3;
            int i2 = (i + 2) % 3;
            if (colors[i] > colors[i1] + colors[i2]) {
                possible = false;
                break;
            }
        }
        if (!possible) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }
        vector<int> sol;
        while (N > 0) {
            if (!sol.empty()) {
                if (sol.front() != sol.back()) {
                    int i = sol.front();
                    int i1 = (i + 1) % 3;
                    int i2 = (i + 2) % 3;
                    if ((colors[i] >= colors[i1]) &&
                        (colors[i] >= colors[i2])) {
                        sol.push_back(i);
                        colors[i]--;
                        N--;
                        continue;
                    }
                }
            }
            int maxPos = 0;
            int maxVal = 0;
            for (int i = 0; i < 3; i++) {
                if (!sol.empty()) {
                    if (sol.back() == i) {
                        continue;
                    }
                }
                if (colors[i] > maxVal) {
                    maxVal = colors[i];
                    maxPos = i;
                }
            }
            sol.push_back(maxPos);
            colors[maxPos]--;
            N--;
        }
        cout << "Case #" << t << ": ";
        for (size_t i = 0; i < sol.size(); i++) {
            if (sol[i] == 0) {
                cout << "R";
            } else if (sol[i] == 1) {
                cout << "Y";
            } else {
                cout << "B";
            }
        }
        cout << endl;
    }
	return 0;
}
