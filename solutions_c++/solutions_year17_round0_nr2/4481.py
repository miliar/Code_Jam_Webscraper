#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;

#define DEBUG

int T;

unsigned long long n;

void solve() {
    cin >> n;

    vector <int> digits;

    while (n > 0) {
        digits.push_back((int) (n % 10));
        n /= 10;
    }

    reverse(digits.begin(), digits.end());

    for (int i = 0; i < digits.size(); ++i) {
        int j = i + 1;
        while (j < digits.size() && digits[j] == digits[i]) {
            ++j;
        }

        if (j == digits.size()) {
            break;
        }

        if (digits[j] > digits[i]) {
            continue;
        }

        --digits[i];
        for (int k = i + 1; k < digits.size(); ++k) {
            digits[k] = 9;
        }

        break;
    }

    unsigned long long ans = 0;
    for (auto d : digits) {
        ans = 10 * ans + d;
    }

    cout << ans;
}

int main() {
    ios::sync_with_stdio(false);

    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}