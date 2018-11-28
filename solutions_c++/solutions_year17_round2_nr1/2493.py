#include <iostream>
#include <iomanip>

using namespace std;

int main() {
//    ios_base::sync_with_stdio(false);
//    cin.tie(NULL);

    int T;
    cin >> T;
    for (int test = 1; test<=T; ++test) {
        double D, K, S, res, max_time = 0.0;
        long long N;
        cin >> D >> N;

        while (N--) {
            cin >> K >> S;
            max_time = max(max_time, (D-K)/S);
        }

        res = D / max_time;

        cout << "Case #" << test << ": " << fixed << setprecision(6) << res << endl;
    }

    return 0;
}