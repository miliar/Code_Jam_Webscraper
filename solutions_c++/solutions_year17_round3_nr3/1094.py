#include <bits/stdc++.h>
using namespace std;

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {

        int N, K; cin >> N >> K;
        double U; cin >> U;

        vector<double> q;
        for (int i = 0; i < N; i++) {
            double x; cin >> x;
            q.push_back(x);
        }

        double minim = 0, maxim = 1.0;
        for (int i = 0; i < 100; i++) {
            double x = (minim + maxim) / 2.0;
            double need = 0;
            for (int k = 0; k < q.size(); k++) {
                if (q[k] > x) continue;
                need += x - q[k];
            }

            if (need <= U) {
                minim = x;
            } else {
                maxim = x;
            }
        }

        double ans = 1.0;
        for (int i = 0; i < N; i++) {
            if (q[i] < minim) q[i] = minim;
            ans *= q[i];
        }

        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(9) << ans << "\n";
    }

    return 0;
}