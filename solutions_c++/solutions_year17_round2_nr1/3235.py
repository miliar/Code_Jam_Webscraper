#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

void solve() {
    int D, n;
    cin >> D >> n;
    vector<pii> K(n);

    for (int i = 0; i < n; i++) {
        cin >> K[i].first >> K[i].second;
    }

    sort(K.begin(), K.end(), greater<pii>());

    double ans = 0;
    for (int i = 0; i < n; i++) {
        double spd = (double)(D - K[i].first) / K[i].second;
        if (spd > ans) ans = spd;
    }

    printf("%.10f\n", D / ans);
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}