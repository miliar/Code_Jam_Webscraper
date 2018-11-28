#include <bits/stdc++.h>

using namespace std;

tuple<int, int, int> f(int l, int r) {
    int mid = (l + r) / 2;
    int d1 = mid - l - 1, d2 = r - mid - 1;
    return make_tuple(-min(d1, d2), -max(d1, d2), mid);
}

void solve(int case_number) {
    int n, k;
    cin >> n >> k;
    set< tuple<int, int, int> > q;
    set<int> used = {0, n + 1};
    q.insert(f(0, n + 1));
    while (used.size() < k + 2 - 1) {
        //assert(!q.empty());
        int pos = get<2>(*q.begin());
        q.erase(q.begin());
        auto it = used.upper_bound(pos);
        assert(it != used.end() && it != used.begin());
        int right = *it;
        int left = *prev(it);
        used.insert(pos);
        //cerr << pos << ' ' << left << ' ' << right << endl;
        if (pos - left > 1) {
            auto tmp = f(left, pos);
            q.insert(tmp);
        }
        if (right - pos > 1) {
            auto tmp = f(pos, right);
            q.insert(tmp);
        }
    }
    //cerr << get<2>(*q.begin()) << endl;
    cout << "Case #" << case_number << ": ";
    cout << -get<1>(*q.begin()) << ' ' << -get<0>(*q.begin()) << '\n';
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
