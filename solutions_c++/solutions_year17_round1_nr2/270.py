#include <bits/stdc++.h>
using namespace std;
const int maxn = 55;

int n, p, a[maxn];
priority_queue<pair<int, int>> packages[maxn];

pair<int, int> servings(int ss, int net) {
    if (10 * net < 9 * ss) {
        return {-1, -2};
    }

    pair<int, int> ret = {-1, -2};

    long long lo = 1, hi = 2e6;
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (10 * net <= 11 * mid * ss) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    ret.first = lo;

    lo = 1, hi = 2e6;
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        if (9 * mid * ss <= 10 * net) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    ret.second = lo;

    //cout << ss << ", " << net << '\n';
    //cout << ret.first << ", " << ret.second << '\n';

    return ret;
}

bool intersect(pair<int, int> p1, pair<int, int> p2) {
    return (p1.first <= p2.first && p2.first <= p1.second)
        || (p2.first <= p1.first && p1.first <= p2.second);
}

int solve() {
    cin >> n >> p;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        packages[i] = priority_queue<pair<int, int>>();
        for (int j = 0; j < p; j++) {
            int net;
            cin >> net;

            auto r = servings(a[i], net);
            if (r.first <= r.second) {
                packages[i].push(r);
            }
        }
    }

    int tot = 0;
    while (!packages[0].empty()) {
        auto r = packages[0].top();

        bool good = true;
        for (int i = 1; i < n; i++) {
            while (!packages[i].empty()) {
                auto cur = packages[i].top();
                if (r.second < cur.first) {
                    packages[i].pop();
                } else {
                    break;
                }
            }
            if (packages[i].empty()) {
                return tot;
            }

            auto cur = packages[i].top();
            if (!intersect(r, cur)) {
                good = false;
                break;
            }
        }

        packages[0].pop();
        if (!good) {
            continue;
        }
        ++tot;
        for (int i = 1; i < n; i++) {
            packages[i].pop();
        }
    }
    return tot;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        cout << solve() << '\n';
        cerr << i << endl;
    }
    return 0;
}
