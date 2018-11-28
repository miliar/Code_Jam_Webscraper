#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <iomanip>

using namespace std;

const double EPS = 1e-9;

void solve() {
    int N, K;
    cin >> N >> K;
    double u;
    cin >> u;
    vector<double> p(N + 1);
    for (int i = 0; i < N; i++) {
        cin >> p[i];
    }
    p[N] = 1;
    
    sort(p.begin(), p.end());

    if (N != K) {
        cout << "Too difficult to solve" << endl;
        return;
    }
    
    for (int i = 0; i < N; i++) {
        if (abs(p[i + 1] - p[i]) < EPS) continue;
        if ((i + 1) * (p[i + 1] - p[i]) < u) {
            u -= (i + 1) * (p[i + 1] - p[i]);
            for (int j = 0; j <= i; j++) {
                p[j] = p[i + 1];
            }
        } else {
            double d = u / (i + 1);
            for (int j = 0; j <= i; j++) {
                p[j] += d;
            }
            break;
        }
    }
    double ans = 1;
    for (int i = 0; i < N; i++) {
        ans *= p[i];
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