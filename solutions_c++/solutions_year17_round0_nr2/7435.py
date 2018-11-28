#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    freopen("/home/nimloth/coding/6sem/codejam/B-large (3).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        long long n;
        cin >> n;
        long long ans = n;
        for (int z = 0; z < 22; z++) {
            vector<long long> digits;
            long long a, d;
            d = ans % 10;
            a = ans / 10;
            while (a != 0 || d != 0) {
                digits.push_back(d);
                d = a % 10;
                a = a / 10;
            }
            reverse(digits.begin(), digits.end());
            long long prev = digits[0];
            long long cur = -1;
            for (int i = 1; i < digits.size(); i++) {
                if (prev <= digits[i]) {
                    prev = digits[i];
                    continue;
                } else {
                    cur = i;
                    break;
                }
            }
            if (cur != -1) {
                long long v;
                v = digits[cur];
                for (int i = cur + 1; i < digits.size(); i++) {
                    v = v * 10 + digits[i];
                }
                ans = ans - (v + 1);
            } else {
                ans = ans;
            }
        }

        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}