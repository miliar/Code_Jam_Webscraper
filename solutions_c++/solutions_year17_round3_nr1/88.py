#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 2017;
const long double PI = 3.1415926535897;

int tc, n, k;
long long r[MAX_N], h[MAX_N], m[MAX_N];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout.precision(20);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
            m[i] = r[i] * h[i];
        }
        long double ans = 0;
        for (int i = 0; i < n; i++) {
            vector<long long> vec;
            for (int j = 0; j < n; j++) {
                if (i != j && r[j] <= r[i]) {
                    vec.push_back(-m[j]);
                }
            }
            sort(vec.begin(), vec.end());
            if (vec.size() + 1 < k) {
                continue;
            }
            long double sum = PI * r[i] * r[i] + PI * 2 * m[i];
            for (int j = 0; j < k - 1; j++) {
                sum += PI * 2 * (-vec[j]);
            }
            ans = max(ans, sum);
        }
        cout << (double) ans << "\n";
    }
}
