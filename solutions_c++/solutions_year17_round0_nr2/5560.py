#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <list>
#include <string>
#include <algorithm>
#include <chrono>
#include <limits>
#include <cmath>
#include <unordered_set>
#include <set>

using namespace std;
using ll = long long;

ll ipow(ll p) {
    ll x = 1;
    while (p--) x *= 10;
    return x;
}

ll get_sub(ll xx) {
    ll t = xx;
    int dc = 0;
    while (t) {
        t /= 10;
        ++dc;
    }
    for (int i = dc; i >= 2; --i) {
        ll x = xx % ipow(i);
        ll l = x / ipow(i - 1);
        ll r = x % ipow(i - 1);
        ll ans = r + 1;
        r /= ipow(i - 2);
        if (l > r) return ans;
    }

    return -1;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        ll x;
        cin >> x;

        ll sub = get_sub(x);
        while (sub != -1) {
            x -= sub;
            sub = get_sub(x);
        }

        cout << "Case #" << t + 1 << ": " << x << endl;
    }
    return 0;
}
