#include "bits.h"
using namespace std;

typedef long long ll;

double max(double a, double b) {
    return a > b ? a : b;
}

void solve() {
    ll D, N;
    cin >> D >> N;

    double time = -1;
    while (N--) {
        ll K, S;
        cin >> K >> S;

        double T = (D-K)/double(S);

        time = max(time, T);
        
    }
    cout << setprecision(12) << double(D)/time;
    
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
