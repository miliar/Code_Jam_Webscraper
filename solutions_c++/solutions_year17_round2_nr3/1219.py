#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i+1 << ": ";
        int n, q;
        cin >> n >> q;
        vector<pair<int, int>> horses(n);
        for (auto &j : horses)
            cin >> j.first >> j.second;
        vector<vector<int>> d(n, vector<int>(n));
        for (auto &j : d)
            for (auto &jj : j)
                cin >> jj;
        vector<pair<int, int>> routes(q); // q == 1
        for (auto &j : routes) 
            cin >> j.first >> j.second;
        vector<vector<pair<double, int>>> dyn(n, vector<pair<double, int>>(n));
        dyn[0][0] = mp(0, horses[0].first);
        for (int j = 0; j < n-1; ++j) {
            double mn = 1e15;
            for (int k = 0; k <= j; ++k) {
                double t = d[j][j+1]/(double)horses[k].second;
                if (dyn[j][k].second >= d[j][j+1]) {   
                    dyn[j+1][k] = mp(dyn[j][k].first + t, dyn[j][k].second - d[j][j+1]);
                    mn = min(dyn[j+1][k].first, mn);
                } else
                    dyn[j+1][k] = mp(1e15, 0); 
            }
            dyn[j+1][j+1] = mp(mn, horses[j+1].first);
        }
        double mn = 1e15;
        for (int k = 0; k < n; ++k) {
            mn = min(mn, dyn[n-1][k].first);
        }
        cout << mn;
        cout << '\n';
    }
    return 0;
}
