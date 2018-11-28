#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;


int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ":";

        int n, p;
        cin >> n >> p;
        int a[5] = {0};
        for (int i = 0; i < n; ++i) {
            int t;
            cin >> t;
            t %= p;
            ++a[t];
        }
        int sol = a[0];
        if (p == 2) {
            sol += (a[1] + 1) / 2;
        } else if (p == 3) {
            int t = min(a[1], a[2]);
            sol += t;
            a[1] -= t;
            a[2] -= t;
            sol += (a[1] + 2) / 3;
            sol += (a[2] + 2) / 3;
        } else if (p == 4) {
            int a13 = min(a[1], a[3]);
            sol += a13;
            a[1] -= a13;
            a[3] -= a13;
            int a2 = a[2] / 2;
            sol += a2;
            a[2] -= a2 * 2;
            int a12 = min(a[1] / 2, a[2]);
            sol += a12;
            a[1] -= a12 * 2;
            a[2] -= a12;
            int a23 = min(a[2], a[3] / 2);
            sol += a23;
            a[3] -= a23 * 2;
            a[2] -= a23;

            int a1 = a[1] / 4;
            sol += a1;
            a[1] -= 4 * a1;
            int a3 = a[3] / 4;
            sol += a3;
            a[3] -= 4 * a3;

            if (a[1] + a[2] + a[3] > 0) {
                ++sol;
            }
        }
        cout << " " << sol << endl;
    }
}
