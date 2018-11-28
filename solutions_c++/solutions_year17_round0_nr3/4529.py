#include <bits/stdc++.h>

using namespace std;

#define gcj cout << "Case #" << Test << ": "

struct Segment {
    long long le, ri;

    Segment() = default;

    bool operator < (const Segment& other) const {
        if (ri - le != other.ri - other.le) {
            return ri - le > other.ri - other.le;
        }
        return le > other.le;
    }
};

int main() {
    
    int tests;
    cin >> tests;
    for (int Test = 1; Test <= tests; ++Test) {
        // cout << "NEW TEST\n\n";
        long long n, k;
        cin >> n >> k;
        if (n == k) {
            gcj;
            cout << 0 << ' ' << 0 << '\n';
            continue;
        }
        set<Segment> q;
        q.insert({1LL, n});
        long long ans1 = 0, ans2 = 0;
        while (k --> 0) {
            auto it = q.begin();
            long long le = (*it).le, ri = (*it).ri;
            q.erase(q.begin());
            if (le == ri) {
                ans1 = 0, ans2 = 0;
            } else {
                long long dist = ri - le;
                if (dist == 1) {
                    q.insert({ri, ri});
                    ans1 = 1, ans2 = 0;
                } else if (dist == 2) {
                    q.insert({le, le});
                    q.insert({ri, ri});
                    ans1 = 1, ans2 = 1;
                } else {
                    q.insert({le, le + dist / 2 - 1});
                    q.insert({le + dist / 2 + 1, ri});
                    ans1 = dist / 2, ans2 = ri - le - dist / 2;
                }
            }
            // vector <int> a(n + 2, 0);
            // for (auto it1 = q.begin(); it1 != q.end(); ++it1) {
            //     long long ll = (*it1).le, rr = (*it1).ri;
            //     for (int j = ll; j <= rr; ++j) {
            //         a[j] = 1;
            //     }
            // }
            // a[0] = 2;
            // a.back() = 2;
            // for (auto el : a) {
            //     cout << el;
            // }
            // cout << '\n';
            // cout << "NEXT ITERATION\n";
        }
        gcj;
        cout << max(ans2, ans1) << ' ' << min(ans1, ans2) << '\n';

    }
}