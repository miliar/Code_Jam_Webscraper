#include <iostream>
#include <vector>
#include <iomanip>

#define forn(i, n) for(int i = 0; i < n; ++i)
#define fore(i, a, b) for(int i = a; i < b; ++i)

using namespace std;

void test(int tNum) {
    int d, n;
    cin >> d >> n;
    double maxT = 0;
    int k, s;
    forn(i, n) {
        cin >> k >> s;
        double tmp = d - k;
        tmp /= s;
        maxT = max(maxT, tmp);
    }
    cout << "Case #" << tNum << ": ";
    cout << fixed << setprecision(20) << d / maxT << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    forn(i, t) {
        test(i + 1);
    }
    return 0;
}

