#include <bits/stdc++.h>
#define int long long
#define double long double
#define eps 1e-9
#define inf 1e15
#define fs first
#define sc second
#define pi acos(-1)

using namespace std;

void solve(int x) {
    int N, K;
    cin >> N >> K;
    int R[N], H[N];
    for (int i = 0; i < N; i++) {
        cin >> R[i] >> H[i];
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
        vector <int> a;
        for (int j = 0; j < N; j++) {
            if (R[j] <= R[i] && i != j) {
                a.push_back(2 * R[j] * H[j]);
            }
        }
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        int just = R[i] * (R[i] + 2 * H[i]);
        if (a.size() < K - 1) continue;
        for (int j = 0; j < K - 1; j++) {
            just += a[j];
        }
        ans = max(ans, just);
    }
    cout << "Case #" << x << ':' << ' ';

    cout << fixed << setprecision(10) << (double)ans * pi;
    cout << '\n';
}


signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
