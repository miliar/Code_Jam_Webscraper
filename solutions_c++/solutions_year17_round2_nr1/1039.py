/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    cout.precision(20);
    for (int T = 1; T <= TN; T++) {
        int n, d;
        cin >> d >> n;
        double t = -d;
        for (int i = 0; i < n; ++i) {
            int k, s;
            cin >> k >> s;
            t = max(t, double(d - k) / s);
        }
        cout << "Case #" << T << ": " << (d / t) << endl;
    }
    return 0;
}
