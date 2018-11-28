#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

typedef pair<int, int> horse;


long double solve(int d, const vector<horse>& horses) {
    long double time = -1;
    for(int i = horses.size()-1; i > 0; --i) {
        long double dist = d-horses[i].first;
        if(time == -1 || dist/time > horses[i].second) {
            time = dist/horses[i].second;
        }
    }
    return d/time;
}

int main() {
    cout << fixed;
    cout << setprecision(6);
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int d, n;
        cin >> d >> n;
        vector<horse> horses(n+1);
        horses[0] = horse(0, INT_MAX);
        for(int j = 1; j <= n; ++j) {
            cin >> horses[j].first >> horses[j].second;
        }
        sort(horses.begin(), horses.end());
        cout << "Case #" << i << ": " << solve(d, horses) << endl;
    }
}