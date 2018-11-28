#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        ll n, k;
        cin >> n >> k;

        map<ll, ll> lens;
        lens[n] = 1;

        ll k_iter = 0;
        while (!lens.empty()) {
            k_iter += lens.rbegin()->second;
            ll max, min;
            min = (lens.rbegin()->first - 1) / 2;
            max = lens.rbegin()->first - 1 - min;
            lens[min] += lens.rbegin()->second;
            lens[max] += lens.rbegin()->second;
            lens.erase(lens.rbegin()->first);
            if (k_iter >= k) {
                cout << "Case #" << test << ": " << max << ' ' << min << endl;
                break;
            }
        }

    }

    return 0;
}
