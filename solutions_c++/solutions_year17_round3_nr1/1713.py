#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Cake {
    int id = 0;
    double r = 0;
    double h = 0;
};

struct RCmp {
    bool operator() (const Cake& a, const Cake& b) const {
        return a.r < b.r;
    }
};

struct HCmp {
    bool operator() (const Cake& a, const Cake& b) const {
        return b.h < a.h;
    }
};


int main() {
    int tests;
    cin >> tests;

    for (int t = 1; t <= tests; t++) {
        int n, k;
        cin >> n >> k;
        multiset<Cake, RCmp> rs;
        multiset<Cake, HCmp> hs;

        for (int i = 0; i < n; ++i) {
            double h, r;
            cin >> r >> h;
            rs.insert({i, r * r, 2.0 * r * h});
            hs.insert({i, r * r, 2.0 * r * h});
        }

        double min_r = 0.0;
        auto start = rs.begin();
        {
            int i = 0;
            for (const Cake& c : rs) {
                i++;
                if (i == k) {
                    min_r = c.r;
                    break;
                }
            }
        }

        while (true) {
            if (start->r == min_r) {
                break;
            } else {
                start++;
            }
        }

        double max = 0.0;
        for (; start != rs.end(); ++start) {
            double cur = start->r + start->h;

            int kk = 0;
            for (const Cake& hc : hs) {
                if (hc.r <= start->r && hc.id != start->id) {
                    kk++;
                    if (kk == k) {
                        break;
                    }
                    cur += hc.h;
                }
            }
            if (cur > max) {
                max = cur;
            }
        }

        printf("Case #%d: %.7f\n", t, max * M_PI);
    }

    return 0;
}
