#include <bits/stdc++.h>
using namespace std;

long long n;
vector<int> digits;

void solve() {
    digits.clear();

    cin >> n;
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    reverse(digits.begin(), digits.end());

    long long res = 0;
    for (size_t i = 0; i < digits.size(); i++) {
        int d = digits[i];

        bool good = true;
        for (size_t j = i + 1; j < digits.size(); j++) {
            if (d < digits[j]) {
                break;
            } else if (d > digits[j]) {
                good = false;
                break;
            }
        }

        if (good) {
            res = 10 * res + d;
        } else {
            res = 10 * res + d - 1;
            for (size_t j = i + 1; j < digits.size(); j++) {
                res = 10 * res + 9;
            }
            break;
        }
    }

    cout << res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
        cerr << i << endl;
    }
    return 0;
}
