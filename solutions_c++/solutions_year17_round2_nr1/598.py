#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int testCases;
    cin >> testCases;

    for (int testCase = 1; testCase <= testCases; testCase++) {
        double d, n;
        cin >> d >> n;

        double last = 0.0;

        for (int i = 0; i < n; i++) {
            double k, s;
            cin >> k >> s;
            
            last = max(last, (d - k) / s);
        }

        double ans = d / last;

        cout << fixed << setprecision(9) << "Case #" << testCase << ": " << ans << endl;
    }
}
