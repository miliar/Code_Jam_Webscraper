#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long solve(long long x) {
    long long xx = x;
    vector<int> xd;
    while (x > 0) {
        xd.push_back(x % 10);
        x /= 10;
    }
    reverse(xd.begin(), xd.end());

    bool ok = true;
    for (int i = 0; i + 1 < xd.size(); i++) {
        if (xd[i] > xd[i + 1]) {
            ok = false;
            break;
        }
    }

    if (ok) {
        return xx;
    }

    long long mx = 0;

    for (int len = xd.size(); len > 0; len--) {
        for (int cp = xd.size() - 1; cp >= 0; cp--) {
            for (int val = xd[cp] - 1; val >= 0; val--) {
                vector<int> y;
                for (int i = 0; i < cp; i++) {
                    y.push_back(xd[i]);
                }
                y.push_back(val);
                while (y.size() < len) {
                    y.push_back(9);
                }
                // xd[0], xd[1], ..., xd[cp - 1], val, ???
                bool ok = true;
                for (int j = 0; j + 1 < y.size(); j++) {
                    if (y[j] > y[j + 1]) {
                        ok = false;
                        break;
                    }
                }

                if (ok) {
                    long long ans = 0;
                    for (int yv : y) {
                        ans *= 10;
                        ans += yv;
                    }

                    return ans;
                }
            }
        }
    }
}

int main() {
    freopen("b1.in", "r", stdin);
    freopen("b1.out", "w", stdout);

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        long long x;
        cin >> x;
        cout << "Case #" << tt << ": " << solve(x) << endl;
    }

    return 0;
}