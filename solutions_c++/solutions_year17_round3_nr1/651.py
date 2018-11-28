#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

const int maxn = 1111;

double dp[maxn][maxn];

struct valType {
    double r, h;
}a[maxn];

const double pi = 3.141592653589793238;

int main() {
    freopen("al.txt", "r", stdin);
    freopen("alout.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        int n, k;
        vector<pair<double, double> > vec;
        cin >> n >> k;
        for (int i = 1; i <= n; ++i) {
            double r, h;
            cin >> r >> h;
            vec.push_back(make_pair(r, h));
        }
        for (int i = 1; i <= n; ++i) {
            a[i].r = vec[i - 1].first;
            a[i].h = vec[i - 1].second;
        }
        double ans = 0;
        for (int i = 1; i <= n; ++i) {
            vector<double> vec;
            for (int j = 1; j <= n; ++j) {
                if (i == j) continue;
                vec.push_back(a[j].r * a[j].h);
            }
            sort(vec.begin(), vec.end());
            reverse(vec.begin(), vec.end());
            double val = a[i].r * a[i].r * pi + a[i].r * a[i].h * pi * 2;
            for (int j = 0; j < k - 1; ++j) {
                val += vec[j] * 2 * pi;
            }
            ans = max(ans, val);
        }
        printf("Case #%d: %.6lf\n", ++ca, ans);
    }
    return 0;
}