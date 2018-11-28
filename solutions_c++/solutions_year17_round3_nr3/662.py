#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int test_number) {
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector<double> p(n);
    for (int i=0; i<n; ++i) {
        cin >> p[i];
    }

    sort(p.begin(), p.end());
    double x;
    for (int i=0; i<n-1; ++i) {
        x = min(u, (p[i+1] - p[i]) * (i + 1));
        for (int j = 0; j < i + 1; ++j) {
            p[j] += x / (i + 1);
        }
        u -= x;
    }
    for (int i=0; i<n; ++i) {
        p[i] += u / n;
    }

    double ans = 1;
    for (int i=0; i<n; ++i) {
        ans *= p[i];
    }

    printf("Case #%d: %.9f\n", test_number, ans);
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
        solve(t);


    return 0;
}
