#include <iostream>
#include <iomanip>
using namespace std;

#define EPS 1e-8

int T;
int N, K;
double U;
double P[50];

bool ok(double P[50], int N, double U, double threshold) {
    double need = 0;
    for (int i = 0; i < N; ++i) {
        if (P[i] < threshold) {
            need += threshold - P[i];
        }
    }
    return need < U + EPS;
}

int main() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);

    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        cin >> N >> K;
        cin >> U;
        for (int i = 0; i < N; ++i) {
            cin >> P[i];
        }

        if (N == K) {
            double l = 0, r = 1 + EPS;
            while (l + EPS <= r) {
                double mid = (l + r) / 2;
                if (ok(P, N, U, mid)) 
                    l = mid + EPS;
                else
                    r = mid;
            }
            l -= EPS;

            double result = 1;
            for (int i = 0; i < N; ++i) {
                result *= max(P[i], l);
            }
            cout << fixed << setprecision(6) << "Case #" << tid + 1 << ": " << result << endl;
        } else {
            cout << "Case #" << tid + 1 << ": Why it is so fucking hard" << endl;
        }
    }

    return 0;
}