#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

long double solve() {

    long d, n, k, s;
    cin >> d >> n;
    long slowest = 0;
    long double sl = 0, kl = 0;
    for (int i = 0; i < n; i++) {
        cin >> k >> s;
        long double asd = (long double)(d - k) / s;
        if (asd > sl) {
            sl = asd;
        }                
    }    

    return (long double)d / sl;
}

int main() {

    int t, p = 1;
    for (cin >> t; t--;) {
        long double res = solve();
        cout << "Case #" << p++ << ": ";
        printf("%Lf",res);
        cout << endl;
    }

    return 0;
}