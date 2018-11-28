#include <bits/stdc++.h>
using namespace std;

void solve(int Case) {
    double D;
    int N;
    cin >> D >> N;
    // printf("%d-%d\n", D, N);
    // vector<int> K, S;
    double _max = -1;
    for (int i=0;i<N;i++) {
        double k,s;
        cin >> k >> s;
        // K.push_back(k);
        // S.push_back(s);
        // printf("%d %d", k , s);
        _max = max(_max, (D-k)/s);
        // cout << _max << "\n";
    }
    double ans = D / _max;
    printf("Case #%d: %.6lf\n", Case, ans);
    // cout << "Case #" << Case << ": " << ans << "\n";
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i+1);
}