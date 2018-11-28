#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <cmath>

#define PROBLEM   "A-large"

# define PI           3.14159265358979323846

#define fv(v, i)    for (int i = 0; i < (int) v.size(); ++i)
#define fn(n, i)    for (int i = 0; i < n; ++i)

using namespace std;



void solve(int n, int k) {
    vector<pair<double, long long>> rh(n);
    fn(n, i) {
        long long r, h;
        cin >> r >> h;
        rh[i].second = r;
        rh[i].first = 2 * PI * r * h;
    }
    sort(rh.begin(), rh.end());
    
    double base = 0;
    for(int i = n-k+1; i < n; ++i) {
        base += rh[i].first;
    }
    double res = 0;
    fn(n-k+1, i) {
        double c = PI * rh[i].second * rh[i].second + base + rh[i].first;
        res = max(c, res);
    }
    for(int i = n-k+1; i < n; ++i) {
        double c = PI * rh[i].second * rh[i].second + base + rh[n-k].first;
        res = max(c, res);
    }
    
    cout << " " << fixed << setprecision(8) << res;
}

int main(int argc, const char * argv[]) {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, m;
        cin >> n >> m;
        cout << "Case #" << t << ":";
        solve(n, m);
        cout << endl;
    }
    return 0;
}
