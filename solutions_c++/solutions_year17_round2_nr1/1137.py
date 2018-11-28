#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int test_number) {
    double d;
    int n;
    cin >> d >> n;
    double k, s;

    double mx_time = 0;
    for (int i=0; i<n; ++i) {
        cin >> k >> s;
        mx_time = max(mx_time, double(d - k) / s);
    }

    double ans = double(d) / mx_time;
    printf("Case #%d: %.6f\n", test_number, ans);
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
