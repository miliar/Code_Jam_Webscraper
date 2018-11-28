#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool f(double t, int d, const vector<pair<int, int>> &horses)
{
    double lastPos = numeric_limits<double>::infinity();
    for (int i = horses.size() - 1; i >= 0; i--) {
        double pos = t * horses[i].second + horses[i].first;
        lastPos = min(pos, lastPos);
    }

    return lastPos >= d;
}

int main()
{
    int t;
    cin >> t;
    int tc = 1;

    while (t--) {
        int d, n;
        cin >> d >> n;

        vector<pair<int, int>> horses(n);
        for (int i = 0; i < n; i++) {
            cin >> horses[i].first >> horses[i].second;
        }

        sort(horses.begin(), horses.end());

        double l = 0;
        double r = 1e20;

        for (int i = 0; i < 500; i++) {
            double mid = (l + r) / 2.0;
            double t = (d / mid);

            if (f(t, d, horses)) {
                l = mid;
            } else {
                r = mid;
            }
        }

        printf("Case #%d: %.10f\n", tc++, l);
    }

    return 0;
}
