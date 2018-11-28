#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int t, k, n;
pair<int, int> p[1000];

int main() {
    cin >> t;
    for (int c = 0; c ++< t;) {
        cin >> n >> k;
        for (int i = 0; i < n; ++i) cin >> p[i].first >> p[i].second;
        sort(p, p + n);
        long long b = 0;
        for (int m = k; m <= n; ++m) {
            long long a = (long long)p[m-1].first * (long long)p[m-1].first;
            vector<long long> v;
            for (int i = 0; i < m - 1; ++i) v.push_back(2 * (long long)p[i].first * (long long)p[i].second);
            sort(v.begin(), v.end());
            v.push_back(2 * (long long)p[m-1].first * (long long)p[m-1].second);
            for (int i = 0; i < k; ++i) a += v[v.size()-i-1];
            b = max(b, a);
        }
        cout << "Case #" << c << ": " << fixed << setprecision(9) << ((long double)b * (long double)M_PI) << '\n';
    }
}
