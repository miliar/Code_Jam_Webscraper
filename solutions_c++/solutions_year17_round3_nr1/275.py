#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <iomanip>

using namespace std;

const double PI = atan(1) * 4;

void solve() {
    int N, K;
    cin >> N >> K;
    vector<double> r(N), h(N), side(N);
    for (int i = 0; i < N; i++) {
        cin >> r[i];
        cin >> h[i];
        side[i] = h[i] * 2 * r[i] * PI;
    }

    double ans = 0;
    for (int i = 0; i < N; i++) {
        double tmp = 0;
        tmp += side[i] + r[i] * r[i] * PI;
        priority_queue<double> q;
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            q.push(side[j]);
        }
        for (int j = 0; j < K - 1; j++) {
            tmp += q.top();
            q.pop();
        }
        //cerr << tmp << endl;
        ans = max(ans, tmp);
    }
    cout << setprecision(20);
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}