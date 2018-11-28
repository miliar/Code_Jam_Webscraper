#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int T;
int N, K;
long double EPS = 1e-9;
long double U;
long double D[55]; // Delta
long double P[55];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> K;
        cin >> U;
        for (int a = 0; a < N; ++a) {
            cin >> P[a];
            D[a] = 0;
        }
        sort(P, P + N);
        int PTR = 0; // First (PTR) elements are equal
        while ((PTR != N - 1) && (P[PTR + 1] - P[PTR]) <= EPS) ++PTR;
        if (PTR == N - 1) {
            D[0] += U / N;
        } else {
            while (PTR != N - 1 && U > EPS) {
                long double GAP = P[PTR + 1] - P[PTR];
                if (U - GAP * (PTR + 1) > EPS) { // Bring everything to the same height...
                    U -= GAP * (PTR + 1);
                    D[0] += GAP;
                    D[PTR + 1] -= GAP;
                    ++PTR;
                    while ((PTR != N - 1) && (P[PTR + 1] - P[PTR]) <= EPS) ++PTR;
                } else { // Not enough
                    D[0] += U / (PTR + 1);
                    D[PTR + 1] -= U / (PTR + 1);
                    U = 0;
                }
            }
            D[0] += U / N;
        }
        long double ANS = 1;
        for (int a = 0; a < N; ++a) {
            if (a) D[a] += D[a - 1];
            P[a] += D[a];
        }
        for (int a = 0; a < N; ++a) {
            ANS *= P[a];
        }
        cout << "Case #" << TC << ": " << fixed << setprecision(9) << ANS << "\n";
    }
    return 0;
}
