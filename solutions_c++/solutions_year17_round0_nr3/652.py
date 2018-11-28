#include "bits/stdc++.h"
using namespace std;

#define int long long

#undef int
int main() {
    #define int long long
    freopen ("inp.in", "r", stdin);
    freopen ("C.out", "w", stdout);
    int t; cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        long long n, k; cin >> n >> k;
        long long num_odd = 0, num_even = 0;
        if ((n % 2) == 0) {
            num_even++;
        } else {
            num_odd++;
        }
        long long cur = 1;
        long long pw = 1;
        // 5, 2
        // 5-> 2 2, 7 -> 3 3 -> 9 -> 4 4
        for (long long seen = 1; cur < k; seen++) {
            long long new_even = 0, new_odd = 0;
            new_even = num_even;
            new_odd = num_even;
            if ((n % 2) == 1) {
                // n is odd right now
                long long x = (n - 1) / 2;
                if (x % 2 == 0) {
                    new_even += 2LL * num_odd;
                } else {
                    new_odd += 2LL * num_odd;
                }
            } else {
                // n is even right now
                long long x = (n - 2) / 2;
                if (x % 2 == 0) {
                    new_even += 2LL * num_odd;
                } else {
                    new_odd += 2LL * num_odd;
                }
            }
            n /= 2LL;
            cur += (1LL << seen);
            num_odd =  new_odd;
            num_even = new_even;
            pw *= 2LL;
        }
        long long rel = k - pw + 1;
        if ((n % 2) == 1) {
            if (n == 1) {
                num_odd = num_odd + num_even;
                num_even = 0;
            }
            if (num_odd >= rel) {
                long long size_range = n;
                long long x = (n  / 2LL);
                long long y = (n  / 2LL);
                if (x < y) swap(x, y);
                cout << "Case #" << qq << ": " << x << ' ' << y << "\n";
            } else {
                long long size_range = n - 1;
                long long x = (n - 1) / 2LL - 1;
                long long y = (n - 1) / 2LL;
                if (x < y) swap(x, y);
                cout << "Case #" << qq << ": " << x << ' ' << y << "\n";
            }
        } else {
            if (num_even >= rel) {
                long long size_range = n;
                long long x = n / 2LL;
                long long y = n / 2LL - 1;
                if (x < y) swap(x, y);
                cout << "Case #" << qq << ": " << x << ' ' << y << "\n";
            } else {
                long long size_range = n - 1;
                long long x = (n - 1) / 2LL;
                long long y = (n - 1) / 2LL;
                if (x < y) swap(x, y);
                cout << "Case #" << qq << ": " << x << ' ' << y << "\n";
            }
        }
    }
}