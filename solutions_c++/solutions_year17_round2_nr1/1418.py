#include <iostream>
#include <set>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int main() {
    int T;
    cin >> T;
    forn(t, T) {
        int d, n;
        cin >> d >> n;
        double ms = 1e100;
        forn(i, n) {
            long long k, s;
            cin >> k >> s;
            //cerr << 1.0 * (d - k) / s << endl;
            //cerr << 1.0 * d * s / (d - k) << endl;
            ms = min(ms, 1.0 * d * s / (d - k));
        }
        cout << "Case #" << t + 1 << ": " << setprecision(9) << fixed << ms << endl;
    }
}
