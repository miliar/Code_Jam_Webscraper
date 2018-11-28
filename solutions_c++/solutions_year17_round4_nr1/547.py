#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define PRECISION 8

void solve() {
    int n, p;
    cin >> n >> p;
    vector <int> a(n, 0), cp(p, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] = a[i] % p;
        cp[a[i]] += 1;
    }
    if (p == 2) {
        cout <<  cp[0] +
                (cp[1] + 1) / 2;
    } else if (p == 3) {
        cout <<  cp[0] +
                 min(cp[1], cp[2]) +
                (max(cp[1], cp[2]) - min(cp[1], cp[2]) + 2) / 3;
    } else if (p == 4) {
        int r = cp[0] +
                min(cp[1], cp[3]) + cp[2] / 2;
        int d = max(cp[1], cp[3]) - min(cp[1], cp[3]);
        cp[2] = cp[2] % 2;
        if (cp[2] == 0) {
            r += (max(cp[1], cp[3]) - min(cp[1], cp[3]) + 3) / 4;
        } else {
            d -= 2;
            r += 1;
            if (d > 0)
                r += (d + 3) / 4;
        }
        cout << r;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifdef FALSE
    cout << setprecision(PRECISION) << std::fixed;
#endif
    int numberOfTestCases;
    cin >> numberOfTestCases;
    for (int testCase = 1; testCase <= numberOfTestCases; ++testCase) {
        cout << "Case #" << testCase << ": ";
        solve();
        cout << endl;
    }
    return 0;
}