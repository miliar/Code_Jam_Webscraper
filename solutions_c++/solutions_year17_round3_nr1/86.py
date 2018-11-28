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

double pi = 3.1415926535897;

typedef pair<int, int> pr;

struct Solver {
    int n, k;
    vector<pr> v;
    double sol;
    vector<vector<double> > dp;
    Solver() {
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            int r, h;
            cin >> r >> h;
            v.emplace_back(r, h);
        }
        sort(v.begin(), v.end());
        dp.assign(n + 1, vector<double>(n + 1, 0));
    }

    
    double solve() {
        sol = 0;
        for (int i = 0; i < n; ++i) {
            double addition = v[i].second * 2 * pi * v[i].first;
            for (int j = k; j > 0; --j) {
                double curArea = dp[i][j];
                if (dp[i + 1][j] < curArea) {
                    dp[i + 1][j] = curArea;
                }
                if (dp[i + 1][j - 1] < curArea + addition) {
                    dp[i + 1][j - 1] = curArea + addition;
                }
                
            }
        }
        for (int i = 1; i <= n; ++i) {
            double area = pi * v[i - 1].first  * v[i - 1].first + dp[i][0];
            if (sol < area) {
                sol = area;
            }
        }
        return sol;
    }
};

int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        Solver solver;
        printf("%.8lf\n", solver.solve());
    }
}
