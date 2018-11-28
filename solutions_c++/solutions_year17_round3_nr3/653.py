#include <bits/stdc++.h>

using namespace std;

int T;


int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, K;
        double U;
        cin >> N >> K >> U;
        vector<double> P;
        vector<double> Ps;
        vector<double> Cost;
        for (int i = 0; i < N; ++i) {
            double p;
            cin >> p;
            P.push_back(p);
        }
        sort(P.begin(), P.end());
        Ps.push_back(P[0]);
        for (int i = 1; i < N; ++i) {
            Ps.push_back(Ps[i-1] + P[i]);
        }
        
        for (int i = N-1; i >= 0; --i) {
            if (U >= P[i]*(i+1) - Ps[i]) {
                double e = U - (P[i]*(i+1) - Ps[i]);
                e /= (i+1);
                double Px = P[i] + e;
                for (int j = 0; j <= i; ++j) P[j] = Px;
                break;
            }
        }

        double pf = 1;
        for (int i = 0; i < N; ++i) pf *= P[i];

        cout << "Case #" << t << ": " << setprecision(17) << pf << endl;
    }
}
