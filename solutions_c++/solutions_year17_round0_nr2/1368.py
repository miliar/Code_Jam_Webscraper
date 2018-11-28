#include <string>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define all(c) begin(c), end(c)
#define contain(c, v) find(all(c), v) != end(c)

long long solve(long long v) {
    vector<int> d;
    while (v) {
        d.push_back(v % 10);
        v /= 10;
    }
    reverse(all(d));
    long long ans = 0;
    vector<int> ad;

    ad.push_back(0);
    for (auto it : d) ad.push_back(it);

    for (int i = 1; i < ad.size(); i++) {
        if (ad[i] < ad[i - 1]) {
            for (int j = i; j > 0; j--) {
                if (ad[j] < ad[j - 1]) ad[j - 1]--, i--;
            }
            for (int j = i+1; j < ad.size(); j++) {
                ad[j] = 9;
            }
            break;
        }
    }

    for (auto it : ad) {
        ans *= 10;
        ans += it;
    }

    return ans;
}

long long brute_force(long long v) {
    for (auto cur = v; cur; cur--) {
        auto i = cur;
        vector<int> d;
        while (i) {
            d.push_back(i % 10);
            i /= 10;
        }
        bool ok = 1;
        reverse(all(d));
        for (int i = d.size() - 1; i > 0; i--) {
            if (d[i] < d[i - 1]) {
                ok = 0;
                break;
            }
        }
        if (ok) return cur;
    }
    return -1;
}

int main() {
#ifdef D
    // freopen("B.in", "r", stdin);
#endif
    int T;
    cin >> T;
    // for (int i = 1; i <= 10000; i++) {
    //     long long a = solve(i), b = brute_force(i);
    //     if (a != b) {
    //         printf("Wrong at %d(%lld,%lld)\n", i, a, b);
    //     }
    // }
    for (int kase = 1; kase <= T; kase++) {
        long long v; cin >> v;
        cout << "Case #" << kase << ": " << solve(v) << endl;
    }

    return 0;
}