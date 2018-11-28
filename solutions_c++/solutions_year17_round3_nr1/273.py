#include <bits/stdc++.h>

using namespace std;

const double pi = acos(-1.0);

void solve(int t) {
    int n, k;
    cin >> n >> k;
    vector<pair<long long, long long>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first >> a[i].second;
    }
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());

    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        multiset<long long> cur;
        long long sum = a[i].first * a[i].first + 2 * a[i].first * a[i].second;
        //cout << sum << endl;
        for (int j = i + 1; j < n; ++j) {
            long long cur_s = 2 * a[j].first * a[j].second;
            cur.insert(cur_s);
            sum += cur_s;
            if (cur.size() == k) {
                sum -= *cur.begin();
                cur.erase(cur.begin());
            }
        }
        //cout << cur.size() << endl;
        //cout << sum << endl;
        ans = max(ans, sum);
    }
    cout << "Case #" << t << ": " << setprecision(32) << pi * ans << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
