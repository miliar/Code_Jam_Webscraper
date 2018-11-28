#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll computeRecMin(ll n, ll k) {
    if (n == 1 && k == 0) return 0;
    int mid = (n - 1) / 2;
    if (k == mid) return k;
    if (k < mid) return computeRecMin( mid, k);
    else return computeRecMin(n - mid - 1 , k - mid - 1);
}

ll computeRecMax(ll n, ll k) {
    if (n == 1 && k == 0) return 0;
    int mid = (n - 1) / 2;
    if (k == mid) return n/2;
    if (k < mid) return computeRecMax(mid, k);
    else return computeRecMax(n - mid - 1, k - mid - 1);
}

struct Status {
    int l;
    int r;
    int plc;
};

bool operator<(const Status& lhs, const Status& rhs) {
    int lhsmin = min(lhs.l, lhs.r);
    int lhsmax = max(lhs.l, lhs.r);
    int rhsmax = max(rhs.l, rhs.r);
    int rhsmin = min(rhs.l, rhs.r);
    if (lhsmin != rhsmin) return lhsmin > rhsmin;
    if (lhsmax != rhsmax) return lhsmax > rhsmax;
    return lhs.plc < rhs.plc;
}


int main() {
    int t; cin >> t;
    for (int _ = 1; _ <= t; ++_) {
        cout << "Case #" << _ << ": ";
        ll n, k; cin >> n >> k;;
        vector<Status> what;
        for (int plc = 0; plc < n; ++plc) {
            Status cur;
            cur.plc = plc;
            cur.l = computeRecMin(n, plc);
            cur.r = computeRecMax(n, plc);
            what.push_back(cur);
        }
        std::nth_element(what.begin(), what.begin() + k - 1,  what.end());
        cout << what[k - 1].r << " " << what[k - 1].l << endl;
    }
}
