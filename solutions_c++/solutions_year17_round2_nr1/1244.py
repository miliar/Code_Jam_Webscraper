#include <bits/stdc++.h>
using namespace std;

const int kN = 1e3 + 10;
int64_t N, K[kN], S[kN];
double D;

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        cin >> D >> N;
        for (int i = 0; i < N; ++i) cin >> K[i] >> S[i];
        auto IsPossible = [&](double tm) {
            for (int i = 0; i < N; ++i) {
                double d = tm * S[i] + K[i];
                if (d < D) return false;
            }
            return true;
        };
        double lo = 0, hi = 1e18, req = 0.0;
        for (int it = 1; it <= 100; ++it) {
            double mid = (lo + hi) * .5;
            //cout << it << " " << mid << endl;
            if (IsPossible(mid)) {
                req = mid;
                hi = mid;
            } else lo = mid;
        }
        //cout << lo << " " << hi << ": " << req << endl;
        cout << "Case #" << t++ << ": ";
        cout << fixed << setprecision(6) << (D / req) << "\n";
    }
    return 0;
}
