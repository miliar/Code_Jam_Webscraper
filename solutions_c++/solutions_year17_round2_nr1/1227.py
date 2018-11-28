#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

const long double EPS = 1e-9;

int TC;
int D, N;
int K[1005], S[1005];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> TC;
    for (int TT = 1; TT <= TC; ++TT) {
        cin >> D >> N;
        long double ANS = -1;
        for (int a = 0; a < N; ++a) {
            cin >> K[a] >> S[a];
            long double TM = (long double)(D - K[a]) / (long double)S[a];
            if (ANS < 0) ANS = (long double)D / (long double)TM;
            else ANS = min(ANS, (long double)D / (long double)TM);
        }
        cout << "Case #" << fixed << setprecision(9) << TT << ": " << ANS << "\n";
    }
    return 0;
}
