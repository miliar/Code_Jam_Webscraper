#include "bits/stdc++.h"
using namespace std;

vector < int > digits;

int main() {
    freopen ("inp.in", "r", stdin);
    freopen ("B.out", "w", stdout);
    int t; cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        long long n; cin >> n;
        digits.clear();
        while (n) {
            long long d = n % 10;
            n /= 10LL;
            digits.push_back((int) d);
        }
        reverse(digits.begin(), digits.end());
        int m = digits.size();
        int pos = 0, last_seen = -1;
        for (int i = 0; i < m - 1; i++) {
            if (digits[i] != last_seen) {
                last_seen = digits[i];
                pos = i;
            }
            if (digits[i] > digits[i + 1]) {
                digits[pos]--;
                for (int j = pos + 1; j < m; j++) {
                    digits[j] = 9;
                }
                break;
            }
        }
        long long build = 0;
        for (int i = 0; i < m; i++) {
            build *= 10LL;
            build += digits[i];
        }
        cout << "Case #" << qq << ": " << build << "\n";
    }
}