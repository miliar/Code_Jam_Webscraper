#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;

typedef pair<int, int> pr;

int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        int n, p;
        cin >> n >> p;
        vector<int> target(n, 0);
        vector<vector<pr> > v(n);
        for (int i = 0; i < n; ++i) {
            cin >> target[i];
        }
        for (int i = 0; i < n; ++i) {
            int cur = target[i] * 10;
            int curlower = cur - target[i];
            int curupper = cur + target[i];
            for (int j = 0; j < p; ++j) {
                int t;
                cin >> t;
                t *= 10;
                int i1 = t / curupper;
                int i2 = t / curlower;
                if (t % curupper != 0) {
                    ++i1;
                }
                v[i].emplace_back(i1, i2);
            }
            sort(v[i].begin(), v[i].end());
            //cerr << "i: " << i << endl;
            //for (pr c : v[i]) {
            //    cerr << "(" << c.first << ' ' << c.second << ")" << endl;
            //}
        }
        vector<int> indices(n, 0);
        int sol = 0;
        while (true) {
            bool done = false;
            for (int i = 0; i < n; ++i) {
                if (indices[i] >= v[i].size()) {
                    done = true;
                    break;
                }
            }

            if (done) break;

            pr possRange = v[0][indices[0]];
            for (int i = 1; i < n; ++i) {
                pr curpr = v[i][indices[i]];
                possRange.first = max(curpr.first, possRange.first);
                possRange.second = min(curpr.second, possRange.second);
            }
            //cerr << possRange.first << ' ' << possRange.second << endl;
            if (possRange.first <= possRange.second) {
                ++sol;
                for (int i = 0; i < n; ++i) {
                    ++indices[i];
                }
            } else {
                for (int i = 0; i < n; ++i) {
                    pr curpr = v[i][indices[i]];
                    if (curpr.second == possRange.second) {
                        ++indices[i];
                    }
                }
            }
        }
        cout << "Case #" << cc << ": " << sol << endl;
    }
}
