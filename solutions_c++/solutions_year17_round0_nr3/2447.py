#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <string>

using namespace std;

struct Interval {
    long long len;
    long long repeat;

    bool operator <(const Interval& ot) const {
        return len > ot.len;
    }
};

void add(map<long long, long long>& s, long long len, long long repeat) {
    if (len > 0) {
        s[len] += repeat;
    }
}

void solve(int e) {
    cout << "Case #" << e << ": ";

    long long n, k; cin >> n >> k;
    map<long long, long long> s;
    s[n] = 1;

    Interval interval{-1, -1};
    long long split = -1;
    for (;;) {
        pair<long long, long long> p = *--s.end();
        interval = Interval{p.first, p.second};
        s.erase(--s.end());
        split = (interval.len - 1) / 2;

        //cerr << "Current interval: " << interval.len << ' ' << interval.repeat << endl;
        //cerr << "split: " << split << endl;
        if (interval.repeat < k) {
            if (interval.len % 2 == 1) {
                add(s, split, interval.repeat * 2);
            } else {
                add(s, split, interval.repeat);
                add(s, interval.len - split - 1, interval.repeat);
            }
            k -= interval.repeat;
            //cerr << "k: " << k << endl;
        } else {
            break;
        }
    }

    long long a = split;
    long long b = interval.len - split - 1;

    cout << max(a, b) << ' ' << min(a, b) << endl;
}

int main() {
    int t; cin >> t;
    for (int e = 1; e <= t; ++e)
        solve(e);
}
