#include <bits/stdc++.h>

using namespace std;

inline long long mn(long long x) {
    return (x - 1) >> 1;
}

inline long long mx(long long x) {
    return x >> 1;
}

struct compare {
    bool operator()(long long a, long long b) const {
        long long a_mn = mn(a), b_mn = mn(b);
        if (a_mn == b_mn) {
            return mx(a) > mx(b);
        } else {
            return a_mn > b_mn;
        }
    }
};

string solve() {
    long long n, k;
    cin >> n >> k;

    map<long long, long long, compare> intervals;
    intervals[n] = 1;

    while (k) {
        long long interval, count;
        tie(interval, count) = *intervals.begin();

        if (count >= k) {
            return to_string(mx(interval)) + " " + to_string(mn(interval));
        }

        k -= count;
        intervals[mx(interval)] += count;
        intervals[mn(interval)] += count;
        intervals.erase(intervals.begin());
    }

    return "Should never be here";
}

int main() {
    int t;
    cin >> t;

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": " << solve() << endl;
    }
}
