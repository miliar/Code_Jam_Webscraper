#include <bits/stdc++.h>

using namespace std;

struct Segment {
    long long l, r;

    Segment() {}

    Segment(long long l, long long r):
            l(l), r(r) {}

    inline long long getFirst() {
        return ((r - l - 1ll) / 2ll);
    }

    inline long long getSecond() {
        return ((r - l) / 2ll);
    }

    inline long long getPos() {
        return (l + getFirst());
    }
};

inline long long getFirst(Segment const& a) {
    return ((a.r - a.l - 1ll) / 2ll);
}

inline long long getSecond(Segment const& a) {
    return ((a.r - a.l) / 2ll);
}

inline bool operator<(Segment const& a, Segment const& b) {
    return (getFirst(a) > getFirst(b) || (getFirst(a) == getFirst(b) && (getSecond(a) > getSecond(b) || (getSecond(a) == getSecond(b) && a.l < b.l))));
}

inline void solve() {
    long long n, k;
    cin >> n >> k;
    set<Segment> s;
    s.insert(Segment(0, n));

    for (int i = 0; i < k; i++) {
        auto segment = (*s.begin());
        s.erase(s.begin());

        if (segment.l != segment.getPos())
            s.insert(Segment(segment.l, segment.getPos()));

        if (segment.getPos() + 1ll < segment.r)
            s.insert(Segment(segment.getPos() + 1ll, segment.r));

        if (i + 1 == k)
            cout << segment.getSecond() << ' ' << segment.getFirst() << endl;
    }

    s.clear();
}

int main() {
    ios_base::sync_with_stdio(false);

#ifdef SCHEMTSCHIK
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else

#endif

    int T;
    cin >> T;

    for (int I = 0; I < T; I++) {
        cout << "Case #" << I + 1 << ": ";
        solve();
    }

    return 0;
}
