#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 2000;
long double dp[MAXN][MAXN];

long double sb(long double r, long double h) {
    return 2 * M_PI * r * h;
}

long double sr(long double r) {
    return M_PI * r * r;
}

int main() {

    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int q;
    cin >> q;
    cout.precision(20);
    for (int t = 0; t < q; t++) {
        int n, k;
        cin >> n >> k;
        vector<long double> r(n), h(n);
        for (int i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
        }

        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (r[i] * h[i] < r[j] * h[j]) {
                    swap(r[i], r[j]);
                    swap(h[i], h[j]);
                }

        long double res = 0;
        for (int i = 0; i < n; i++) {
            long double sum = sb(r[i], h[i]) + sr(r[i]);
            int k1 = 1;
            for (int j = 0; i < n; j++) {
                if (k1 == k)
                    break;
                if (i != j && r[j] <= r[i]) {
                    k1++;
                    sum += sb(r[j], h[j]);
                }
            }
            res = max(res, sum);
        }
        cout << "Case #" << t + 1 << ": " << res << "\n";
    }

    return 0;
}